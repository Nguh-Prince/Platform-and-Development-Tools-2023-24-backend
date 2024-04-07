import os

from models.exams import Exam
from .files import save_file

from werkzeug.utils import secure_filename

from constants import UPLOAD_FOLDER

def get_all_exams(return_objects=False):
    """
    Set return_objects to True if you want to return a 
    model instance instead of JSON
    """
    objects = Exam.read()

    if not return_objects:
        list_of_objects = [
            obj.toJSON() for obj in objects
        ]
        return list_of_objects
    
    return objects

def get_exam_with_id(id, return_object=False):
    """
    Set return_object to True if you want to return a 
    model instance instead of JSON
    """
    obj = Exam.read(id)

    return obj if return_object else obj.toJSON()

def save_exam(subject, academic_year, session, duration, id=None, uploaded_files=None, return_object=False):
    if id != None:
        exam = get_exam_with_id(id, return_object=True)
        exam.subject, exam.academic_year, exam.session, exam.duration = (
            subject, academic_year, session, duration
        )
    else:
        exam = Exam(
            subject=subject,academic_year=academic_year, 
            session=session, duration=duration
        )

    exam.save()

    for file in uploaded_files:
        file_name = secure_filename(file.filename)

        save_file(exam=exam.id, path=file_name)

        file.save(
            os.path.join(UPLOAD_FOLDER, file_name)
        )

    return exam if return_object else exam.toJSON()
    
def delete_exam(id):
    exam = get_exam_with_id(id)
    exam.delete()

    return exam.toJSON()