from models.files import File

def get_all_files():
    return File.read()

def get_file_with_id(id):
    return File.read(id)

def save_file(exam, path, id=None):
    if id != None:
        file = get_file_with_id(id)
        file.exam, file.path = exam, path

    else:
        file = File(
            exam=exam, path=path
        )

    file.save()

def delete_file(id):
    file = get_file_with_id(id)
    file.delete()