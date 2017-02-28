from mywebsite import app
import re
from redis import Redis
from flask import render_template, request, redirect, jsonify, url_for

redis = Redis(app.config['REDIS_HOST'], app.config['REDIS_PORT'], db=0)

class LinkNotFound(Exception):
    status_code = 404

    def __init__(self, short_id=None, status_code=None, message=None):
        Exception.__init__(self)
        if status_code is not None:
            self.status_code = status_code
        if message is None:
            self.message = short_id+" isn't a valid short id for any url here"
        else:
            self.message = message
        self.short_id = short_id

    def to_dict(self):
        rv = dict()
        rv['short_id'] = self.short_id
        rv['message'] = self.message
        rv['status_code'] = self.status_code
        return rv

@app.route('/shorten/', methods=['GET', 'POST'])
def shorten():
    error = None
    url = None
    if request.method == 'POST':
        url = request.form['url']
        if not is_valid_url(url):
            error = 'Invalid URL'
        else:
            short_id = insert_url(url)
            redirect_url =  url_for('short_link_details', short_id=short_id)
            #return redirect(redirect_url)
            return jsonify(
                short_url=url_for('follow_short_link', short_id=short_id)
                ,click_count = int(redis.get('click-count:' + short_id) or 0)
            )
    url_count = redis.get('last-url-id')
    if not url_count:
        url_count = 0
    return render_template('new_url.html', error=error, url=url, url_count=url_count)

@app.route('/shorten_url_count/')
def url_count():
    url_count = redis.get('last-url-id')
    if not url_count:
        url_count = 0
    return jsonify(url_count=url_count)

@app.route('/shorten/<string:short_id>/')
def follow_short_link(short_id):
    link_target = redis.get('short-link:' + short_id)
    if link_target is None:
        raise LinkNotFound(short_id)
    redis.incr('click-count:' + short_id)
    return redirect(link_target)

@app.route('/shorten/<string:short_id>+/')
def short_link_details(short_id):
    link_target = redis.get('short-link:' + short_id)
    if link_target is None:
        raise LinkNotFound(short_id)
    click_count = int(redis.get('click-count:' + short_id) or 0)
    '''
    return render_template('short_link_details.html',
        link_target=link_target,
        short_id=short_id,
        click_count=click_count
    )
    '''
    return jsonify(
        link_target=link_target,
        short_id=url_for(follow_short_link, short_id=short_id),
        click_count=click_count
    )

@app.errorhandler(LinkNotFound)
def handle_link_not_found(error):
    return render_template('short_link_not_found.html',
        short_id=error.short_id,
        message=error.message
    ), 404

def insert_url(url):
    short_id = redis.get('reverse-url:' + url)
    if short_id is not None:
        return short_id
    url_num = redis.incr('last-url-id')
    short_id = base36_encode(url_num)
    redis.set('short-link:' + short_id, url)
    redis.set('reverse-url:' + url, short_id)
    return short_id

def base36_encode(number):
    assert number >= 0, 'positive integer required'
    if number == 0:
        return '0'
    base36 = []
    while number != 0:
        number, i = divmod(number, 36)
        base36.append('0123456789abcdefghijklmnopqrstuvwxyz'[i])
    return ''.join(reversed(base36))

def is_valid_url(url):
    url_regex = re.compile(
        r'^((?:http|ftp)s?://)' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    is_valid = re.match(url_regex,url)
    if is_valid:
        return True
    else:
        return False