from flask import Blueprint, request

from controllers.subjects import *
from models.exceptions import ModelNotFoundError

from .utils import parse_request_data
from .responses import JSONResponse

subjects_view = Blueprint('subjects', __name__, url_prefix='/subjects')

@subjects_view.route('/', methods=['GET', 'POST'])
def list_or_create():
    if request.method == 'GET':
        return get_all_subjects()
    else:
        submitted_data = parse_request_data(request=request)

        subject = save_subject(submitted_data['name'])
        response = JSONResponse(status=201, content_type="application/json", data=subject)

        return response

@subjects_view.route('/<id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def get_or_update_instance(id):
    instance = None
    try:
        instance = get_subject_with_id(id, return_object=True)
    except ModelNotFoundError:
        return JSONResponse("<h1>Instance not found</h1>", status=404)
    
    if request.method == 'GET':
        return instance
    elif request.method == 'PATCH':
        data = parse_request_data(request)
        return JSONResponse(data=save_subject(name=data['name'], id=instance.id), status=201)
    elif request.method == 'DELETE':
        return JSONResponse(data=delete_subject(id), status=201)
