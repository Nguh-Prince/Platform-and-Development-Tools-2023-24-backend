import sqlite3
import json

from .base_model import AbstractBaseModel

from .constants import PATH_TO_DB

class Exam(AbstractBaseModel):
    TABLE_NAME = "Exam"

    def __init__(self, id=None, subject=None, academic_year=None, session=None, duration=2) -> None:
        self.id = id
        self.subject = subject
        self.academic_year = academic_year
        self.session = session
        self.duration = duration

    def save(self):
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()

            if self.id:
                query = f"UPDATE {self.__class__.TABLE_NAME} SET subject=?, academic_year=?, session=?, duration=? WHERE id=?"
                
                cursor.execute(
                    query,
                    (self.subject, self.academic_year, self.session, self.duration, self.id)
                )
            else:
                # save into the database
                query = f"INSERT INTO {self.TABLE_NAME} (subject, academic_year, session, duration) VALUES (?,?,?,?)"

                cursor.execute(
                    query, 
                    (self.subject, self.academic_year, self.session, self.duration)
                )

                # get the newly created record's id
                id = cursor.execute(f"SELECT MAX(id) FROM {self.TABLE_NAME}").fetchone()[0]

                self.id = id

    def read(id=None):
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()

            if id:
                result = cursor.execute(f"SELECT id, subject, academic_year, session, duration FROM {__class__.TABLE_NAME} WHERE id=?", (id, )).fetchone()

                exam = __class__(id=result[0], subject=result[1], academic_year=result[2], session=result[3], duration=result[4])

                return exam
            else:
                results = cursor.execute(f"SELECT id, subject, academic_year, session, duration FROM {__class__.TABLE_NAME}").fetchall()
                
                exams = []
                
                for result in results:
                    exam = __class__(id=result[0], subject=result[1], academic_year=result[2], session=result[3], duration=result[4])
                    exams.append(exam)

                return exams

    def delete(self):
        with sqlite3.connect(PATH_TO_DB) as connection:
            cursor = connection.cursor()

            cursor.execute(f"DELETE FROM {self.TABLE_NAME} WHERE id=?", (self.id,))

        self.id = None

    def toJSON(self):
        return {
            "id": self.id,
            "subject": self.subject,
            "academic_year": self.academic_year,
            "session": self.session,
            "duration": self.duration
        }
