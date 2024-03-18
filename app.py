import os

from flask import Flask

from views.exams import exams_view
from views.subjects import subjects_view

UPLOAD_FOLDER = os.path.join(
    os.path.dirname(__file__), 
    'uploads'
)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(exams_view)
app.register_blueprint(subjects_view)