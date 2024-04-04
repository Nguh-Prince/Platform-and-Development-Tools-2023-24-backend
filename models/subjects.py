import sqlite3
import json

from .base_model import AbstractBaseModel
from .exceptions import ModelNotFoundError

from .constants import PATH_TO_DB

class Subject(AbstractBaseModel):
    def __init__(self, name, id=None) -> None:
        self.id = id
        self.name = name
        dict.__init__(self, name=name, id=id)
    
    TABLE_NAME = "Subject"

    def __init__(self, id=None, name=None) -> None:
        self.id = id
        self.name = name

    def save(self):
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()

            if self.id:
                query = f"UPDATE {self.__class__.TABLE_NAME} SET name=? WHERE id=?"
                
                cursor.execute(
                    query,
                    (self.name, self.id)
                )
            else:
                # save into the database
                query = f"INSERT INTO {self.TABLE_NAME} (name) VALUES (?)"

                cursor.execute(
                    query, 
                    (self.name,)
                )

                # get the newly created record's id
                id = cursor.execute(f"SELECT MAX(id) FROM {self.TABLE_NAME}").fetchone()[0]

                self.id = id

    def read(id=None):
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()

            if id:
                result = cursor.execute(f"SELECT id, name FROM {__class__.TABLE_NAME} WHERE id=?", (id, )).fetchone()
                
                try:
                    subject = __class__(id=result[0], name=result[1])

                    return subject
                except TypeError:
                    raise ModelNotFoundError
            else:
                results = cursor.execute(f"SELECT id, name FROM {__class__.TABLE_NAME}").fetchall()
                
                subjects = []
                
                for result in results:
                    subject = __class__(id=result[0], name=result[1])
                    subjects.append(subject)

                return subjects

    def delete(self):
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()

            cursor.execute(f"DELETE FROM {self.TABLE_NAME} WHERE id=?", (self.id,))

        self.id = None

    def toJSON(self):
        return {
            "name": self.name,
            "id": self.id
        }
