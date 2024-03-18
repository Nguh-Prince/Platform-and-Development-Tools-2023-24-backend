from models.subjects import Subject

def get_all_subjects():
    subjects = Subject.read()

    return [ subject.toJSON() for subject in subjects ]

def get_subject_with_id(id):
    return Subject.read(id).toJSON()

def save_subject(name, id=None):
    if id != None:
        # get subject with id
        subject = get_subject_with_id(id)
        subject.name = name

    else:
        subject = Subject(name=name)
    
    subject.save()

    return subject.toJSON()

def delete_subject(id):
    subject = get_subject_with_id(id)
    subject.delete()

    return subject.toJSON()
