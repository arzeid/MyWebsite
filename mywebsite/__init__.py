from __future__ import print_function
import sys
import os
from flask import Flask

print(sys.version, file=sys.stderr)

assets_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    import_name = __name__,
    static_folder = os.path.join(assets_path,'static'),
    template_folder = os.path.join(assets_path,'templates'),
    instance_path = os.path.join(assets_path,'instance'),
    instance_relative_config = True,
    root_path = os.path.join(assets_path,__name__)
)

app.config.from_pyfile('deployment.cfg', silent=False)

if not app.debug:
    import logging
    from logging import FileHandler
    file_handler = FileHandler(os.path.join(assets_path,__name__+'.log'))
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)

import mywebsite.shorten
import mywebsite.home