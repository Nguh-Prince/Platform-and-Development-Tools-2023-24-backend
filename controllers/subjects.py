from models.subjects import Subject

def get_all_subjects(return_objects=False):
    subjects = Subject.read()

    if not return_objects:
        list_of_subjects = [
            subject.toJSON() for subject in subjects
        ]
        return list_of_subjects

    return subjects

def get_subject_with_id(id, return_object=False):
    """
    Set return_object to True if you want to return a 
    model instance instead of JSON
    """
    subject = Subject.read(id)
    return subject if return_object else subject.toJSON()

def save_subject(name, id=None):
    if id != None:
        # get subject with id
        subject = get_subject_with_id(id, return_object=True)
        subject.name = name

    else:
        subject = Subject(name=name)
    
    subject.save()

    return subject.toJSON()

def delete_subject(id):
    subject = get_subject_with_id(id, return_object=True)
    subject.delete()

    return subject.toJSON()
