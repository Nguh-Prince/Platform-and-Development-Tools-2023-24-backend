import os

from models.exams import Exam
from .files import save_file

from werkzeug.utils import secure_filename

from constants import UPLOAD_FOLDER

def get_all_exams():
    return Exam.read()

def get_exam_with_id(id):
    return Exam.read(id)

def save_exam(subject, academic_year, session, duration, id=None, uploaded_files=None):
    if id != None:
        exam = get_exam_with_id(id)
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

    return exam
    
def delete_exam(id):
    exam = get_exam_with_id(id)
    exam.delete()