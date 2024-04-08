import sqlite3
import json

from .base_model import AbstractBaseModel

from .constants import PATH_TO_DB

class File(AbstractBaseModel):
    TABLE_NAME = "File"

    def __init__(self, exam, path, id=None) -> None:
        self.id = id
        self.exam = exam
        self.path = path

    def save(self):
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()

            if self.id:
                query = f"UPDATE {self.__class__.TABLE_NAME} SET exam=?, path=? WHERE id=?"
                
                cursor.execute(
                    query,
                    (self.exam, self.path, self.id)
                )
            else:
                # save into the database
                query = f"INSERT INTO {self.TABLE_NAME} (exam, path) VALUES (?,?)"

                cursor.execute(
                    query, 
                    (self.exam, self.path)
                )

                # get the newly created record's id
                id = cursor.execute(f"SELECT MAX(id) FROM {self.TABLE_NAME}").fetchone()[0]

                self.id = id

    def read(id=None, exam_id=None):
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()

            if id:
                result = cursor.execute(f"SELECT id, exam, path FROM {__class__.TABLE_NAME} WHERE id=?", (id, )).fetchone()

                file = __class__(id=result[0], exam=result[1], path=result[2])

                return file
            else:
                results = cursor.execute(f"SELECT id, exam, path FROM {__class__.TABLE_NAME}").fetchall()
                
                files = []
                
                for result in results:
                    file = __class__(id=result[0], exam=result[1], path=result[2])
                    files.append(file)

                return files

    def delete(self):
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()

            cursor.execute(f"DELETE FROM {self.TABLE_NAME} WHERE id=?", (self.id,))

        self.id = None

    def delete_all():
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()

            cursor.execute(f"DELETE FROM {__class__.TABLE_NAME}")

    def toJSON(self):
        return {
            "id": self.id,
            "exam": self.exam,
            "path": self.path
        }