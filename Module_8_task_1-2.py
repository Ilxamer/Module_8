import sqlite3
from datetime import datetime
conn = sqlite3.connect('homewrk.sqlite')

cursor = conn.cursor()

# cursor.execute('CREATE TABLE Students (id int,name VarChar(32),surname VarChar(32),age int,city VarChar(32))')
# cursor.execute('CREATE TABLE Courses (id int,name VarChar(32),time_start datetime,time_end datetime)')
# cursor.execute('CREATE TABLE Student_courses (student_id int,course_id int)')

# conn.commit()
# conn.close()

# cursor.executemany('INSERT INTO Courses VALUES (?,?,?,?)', [(1, 'python', datetime(2021,7,21), datetime(2021,8,21)),(2, 'java', datetime(2021,7,13), datetime(2021,8,16))])
# cursor.executemany('INSERT INTO Students VALUES (?,?,?,?,?)', [(1, 'Max', 'Brooks', 24, 'Spb'),(2, 'John', 'Stones', 15, 'Spb'),
# # (3, 'Andy', 'Wings', 45, 'Manhester'),(4, 'Kate', 'Brooks', 34, 'Spb')])
# cursor.executemany('INSERT INTO Student_courses VALUES (?,?)', [(1,1),(2,1),(3,1),(4,2)])
# conn.commit()

# cursor.execute('SELECT name,surname FROM Students WHERE age > 30 ')
# print(cursor.fetchall())
cursor.execute('SELECT name,surname FROM Students JOIN Student_courses ON Student_courses.student_id = Students.id  WHERE course_id = 1 and city == "Spb"  ')
print(cursor.fetchall())

