from flask import Blueprint, request

from controllers.exams import *
from models.exceptions import ModelNotFoundError

from .utils import parse_request_data
from .responses import JSONResponse, instance_not_found_response

exams_view = Blueprint('exams', __name__, url_prefix='/exams')

@exams_view.route('/', methods=['GET', 'POST'])
def list_or_create():
    if request.method == 'GET':
        return JSONResponse(data=get_all_exams())
    else:
        submitted_data = request.form
        files = request.files.getlist("files")

        subject, session, duration, academic_year = (
            submitted_data['subject'], submitted_data['session'], 
            submitted_data['duration'], submitted_data['academic_year']
        )

        return JSONResponse(data=save_exam(subject, academic_year, session, duration, uploaded_files=files), status=201)
    
@exams_view.route('/<id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def get_or_update_instance(id):
    instance = None
    try:
        instance = get_exam_with_id(id, return_object=True)
    except ModelNotFoundError:
        return instance_not_found_response
    
    if request.method == 'GET':
        return JSONResponse(data=instance)
    elif request.method == 'PATCH':
        submitted_data = request.form
        files = request.files.getlist("files")

        subject, session, duration, academic_year = (
            submitted_data['subject'], submitted_data['session'], 
            submitted_data['duration'], submitted_data['academic_year']
        )

        return JSONResponse(data=save_exam(subject, academic_year, session, duration, uploaded_files=files, id=instance.id), status=201)
    elif request.method == 'DELETE':
        instance.delete()

        return JSONResponse(data=instance, status=200)
    