from mywebsite import app, flat_pages
from flask import render_template
from flask_flatpages import pygments_style_defs

posts_list = []

@app.before_first_request
def generate_posts_list():
    global posts_list
    posts_list = [p for p in flat_pages]
    posts_list.sort(key=lambda item:item['published'], reverse=True)

@app.route("/blog/")
def posts():
    return render_template('blog.html', posts=posts_list)

@app.route('/blog/<name>/')
def post(name):
    post = flat_pages.get_or_404(name)
    return render_template('post.html', post=post)

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('monokai'), 200, {'Content-Type': 'text/css'}

