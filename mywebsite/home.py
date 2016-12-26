from mywebsite import app
from flask import render_template


@app.route('/')
def index():
    return render_template('home.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

