import os

from flask import Flask, send_from_directory

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

# to download images from the server
@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], name)