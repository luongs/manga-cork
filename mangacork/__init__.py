import os
import logging

from flask import Flask

log = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

import mangacork.views
