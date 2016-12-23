from __future__ import print_function
import sys
import os
from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from pygments.styles import get_all_styles

print(sys.version, file=sys.stderr)
print(list(get_all_styles()))

assets_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    import_name = __name__,
    static_folder = os.path.join(assets_path,'static'),
    template_folder = os.path.join(assets_path,'templates'),
    instance_path = os.path.join(assets_path,'instance'),
    instance_relative_config = True,
    root_path = os.path.join(assets_path,__name__)
)

app.config.from_pyfile('development.cfg', silent=False)
app.config['FLATPAGES_ROOT'] = os.path.join(assets_path,'blog')

flat_pages = FlatPages(app)
freezer = Freezer(app)

if not app.debug:
    import logging
    from logging import FileHandler
    file_handler = FileHandler(os.path.join(assets_path,__name__+'.log'))
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)

import mywebsite.shorten
import mywebsite.home
import mywebsite.blog