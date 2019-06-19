import os
import sqlite3

DIR = os.path.dirname(__file__)
DBFILENAME = 'ba.db'
DBPATH = os.path.join(DIR, DBFILENAME)

def seed(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

        #Campuses inserts
        SQL = """INSERT INTO campuses(city, state) VALUES (?,?);"""

        campuses = [
            ("New York", "NY"),
            ("Houston", "TX")
        ]

        for campus in campuses:
            cur.execute(SQL, campus)

        #Students inserts
        SQL = """INSERT INTO students(campuses_pk, first_name, last_name, id, gpa) VALUES (?,?,?,?,?);"""

        students = [
            (1, "Walker", "Lockett", "S000000001", 3.1),
            (1, "Casey", "Coleman", "S000000002", 2.7),
            (1, "Franklyn", "Kilome", "S000000003", 3.8),
            (1, "Hecton", "Santiago", "S000000004", 2.9),
            (2, "Framber", "Valdez", "S000000005", 3.9),
            (2, "Brad", "Peacock", "S000000006", 2.8),
            (2, "Reymin", "Guduan", "S000000007", 3.5),
            (2, "Gerrit", "Cole", "S000000008", 3.0)
        ]

        for student in students:
            cur.execute(SQL, student)

        #Move Gerrit Cole to New York
        SQL = """UPDATE students SET campuses_pk = 1 WHERE first_name = 'Gerrit' AND last_name = 'Cole';"""
        cur.execute(SQL)

        #Retrieve NY students with gpa >3.0
        SQL = """SELECT students.id FROM students, campuses WHERE campuses.pk = students.campuses_pk AND 
                 campuses.city = 'New York' AND students.gpa > 3.0;"""
        cur.execute(SQL)
        print(cur.fetchall())

if __name__ == "__main__":
    seed()
