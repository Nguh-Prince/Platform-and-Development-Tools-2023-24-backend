from flask import Blueprint, request

from controllers.exams import *

exams_view = Blueprint('exams', __name__, url_prefix='/exams')

@exams_view.route('/', methods=['GET', 'POST'])
def list_or_create():
    if request.method == 'GET':
        return get_all_exams()
    else:
        submitted_data = request.POST
        files = request.files.getlist("files")

        subject, session, duration, academic_year = (
            submitted_data['subject'], submitted_data['session'], 
            submitted_data['duration'], submitted_data['academic_year']
        )

        return save_exam(subject, academic_year, session, duration, uploaded_files=files)
    
@exams_view.route('/<id>', methods=['GET', 'POST'])
def get_or_update_instance(id):
    if request.method == 'GET':
        return get_exam_with_id(id)
    pass