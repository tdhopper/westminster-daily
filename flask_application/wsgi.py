import site
import sys
import os
import logging

site.addsitedir(os.path.dirname(__file__))

logging.basicConfig(stream = sys.stderr)

from flask_application import app as application
