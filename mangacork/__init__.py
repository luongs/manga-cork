import os
import logging

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

log = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

import mangacork.views
