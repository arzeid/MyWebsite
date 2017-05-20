from mywebsite import app, workshops_list
from flask import render_template, abort

"""
@app.route('/workshops/')
def workshop_index():
    return render_template('workshops_index.html',workshops=workshops_list)
    abort(404)

@app.route('/workshops/<name>/')
def workshop_view(name):
    clean_name = name.lower().replace('-',' ')
    if clean_name in workshops_list:
    	return render_template('workshop.html',deck_name=clean_name,
                               deck_url=workshops_list[clean_name])
    abort(404)
"""

@app.route('/workshops/<name>')
def slides_view(name):
    clean_name = name.lower().replace('-',' ')
    if clean_name in workshops_list:
        return render_template('slides.html',deck_name=clean_name,
                               deck_url=workshops_list[clean_name])
    abort(404)
