import os

from flask import *
from werkzeug.utils import secure_filename

from .constants import UPLOAD_FOLDER

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        files = request.files.getlist("file")

        for file in files:
            file_name = secure_filename(file.filename)
            file.save(
                os.path.join(UPLOAD_FOLDER, file_name)
            )

        redirect('/')
    
    return render_template('index.html')

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], name)