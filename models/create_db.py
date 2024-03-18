import os
import sqlite3

PATH_TO_DB = os.path.join(
    os.path.dirname(__file__),
    "db.sqlite"
)

create_subject_table_query = "CREATE TABLE subject (name TEXT, id INTEGER PRIMARY KEY AUTOINCREMENT)";

create_exam_table_query = """
CREATE TABLE exam(academic_year TEXT, session TEXT, duration INTEGER, 
id INTEGER PRIMARY KEY AUTOINCREMENT, subject INTEGER, FOREIGN KEY(subject) REFERENCES subject(id))
"""

create_file_table_query = "CREATE TABLE file(path TEXT, id INTEGER PRIMARY KEY AUTOINCREMENT, exam INTEGER, FOREIGN KEY(exam) REFERENCES exam(id))"

with sqlite3.connect(PATH_TO_DB) as connection:
    cursor = connection.cursor()

    for query in [create_subject_table_query, create_exam_table_query, create_file_table_query]:
        cursor.execute(query)    