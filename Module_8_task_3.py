from peewee import * 
from datetime import datetime


conn = SqliteDatabase('orm.sqlite')

class Student(Model):

    student_id = IntegerField(column_name='id', primary_key=True)
    name = CharField(column_name='name')
    surname = CharField(column_name='surname')
    age = IntegerField(column_name='age')
    city = CharField(column_name='city')

    class Meta:
        database = conn


class Course(Model):

    course_id = IntegerField(column_name='id', primary_key=True)
    name = CharField(column_name='name')
    time_start = DateTimeField(column_name='time_start')
    time_finish = DateTimeField(column_name='time_finish')

    class Meta:
        database = conn


class Student_Course(Model):

    student_id = ForeignKeyField(Student, to_field='student_id')
    course_id = ForeignKeyField(Course, to_field='course_id')

    class Meta:
        database = conn





def create_db():
	students = [(1, 'Max', 'Brooks', 24, 'Spb'),
				(2, 'John', 'Stones', 15, 'Spb'),
				(3, 'Andy', 'Wings', 45, 'Manhester'),
				(4, 'Kate', 'Brooks', 34, 'Spb')]
	courses = [(1, 'python', datetime(2021,7,21), datetime(2021,8,21)),(2, 'java', datetime(2021,7,13), datetime(2021,8,16))]
	student_courses = [(1, 1),(2,1),(3,1),(4,2)]

	Student.create_table()
	Course.create_table()
	Student_Course.create_table()

	Student.insert_many(students).execute()
	Course.insert_many(courses).execute()
	Student_Course.insert_many(student_courses).execute()

def queries():
	query_1 = Student.select().where(Student.age > 30)

	for query in query_1:
		print(query.name,query.surname)
		print('Query_1 done')

	query_3 = Student.select().join(Student_Course).join(Course).where((Course.name == 'python') & (Student.city == 'Spb'))
	for query in query_3:
		print(query.name,query.surname)
		print('Query_3 done')


# create_db()
queries()


