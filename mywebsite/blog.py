from mywebsite import app, flat_pages
from flask import render_template
from flask_flatpages import pygments_style_defs

@app.route("/blog/")
def posts():
    posts = [p for p in flat_pages]
    posts.sort(key=lambda item:item['published'], reverse=False)
    return render_template('blog.html', posts=posts)

@app.route('/blog/post/<name>/')
def post(name):
    post = flat_pages.get_or_404(name)
    return render_template('post.html', post=post)

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('monokai'), 200, {'Content-Type': 'text/css'}

