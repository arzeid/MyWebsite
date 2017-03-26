from __future__ import print_function
import os
from flask import Flask
from flask_flatpages import FlatPages
import sys

assets_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    import_name = __name__,
    static_folder = os.path.join(assets_path,'static'),
    template_folder = os.path.join(assets_path,'templates'),
    instance_path = os.path.join(assets_path,'instance'),
    instance_relative_config = True,
    root_path = os.path.join(assets_path,__name__)
)

app.config['FLATPAGES_ROOT'] = os.path.join(assets_path,'blog')
flat_pages = FlatPages(app)

workshops_path = os.path.join(assets_path,'workshops.list')
app.config['WORKSHOPS_PATH'] = workshops_path
workshops_list = dict()
with open(workshops_path,'r') as w_list:
    for line in w_list:
        name,url = line.split('=+=+=')
        clean_name = name.replace('-',' ').lower()
        workshops_list[clean_name] = url 

if os.path.isfile(os.path.join(assets_path,'instance','deployment.cfg')):
    app.config.from_pyfile('deployment.cfg', silent=False)
    print("===deployment config loaded===", file=sys.stderr)
elif os.path.isfile(os.path.join(assets_path,'instance','development.cfg')):
    app.config.from_pyfile('development.cfg', silent=False)
    print("===development config loaded===", file=sys.stderr)
else:
    app.config.update(
        DEBUG = True,
        TESTING = True,
        PROPAGATE_EXCEPTIONS = True,
        REDIS_HOST = 'localhost',
        REDIS_PORT = 6379,
        FLATPAGES_AUTO_RELOAD = 'DEBUG',
        FLATPAGES_EXTENSION = '.md'
    )
    print("===default config loaded===", file=sys.stderr)


if app.debug:
    from pygments.styles import get_all_styles
    print("==="+sys.version+"===", file=sys.stderr)
    #print(list(get_all_styles()))
else:
    import logging
    from logging import FileHandler
    file_handler = FileHandler(os.path.join(assets_path,__name__+'.log'))
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)

import mywebsite.shorten
import mywebsite.home
import mywebsite.blog
import mywebsite.workshop