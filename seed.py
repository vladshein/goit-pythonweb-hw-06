from models.models import Base, Student, Teacher, Subject, Grade, Group
from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import DB_CONNECTION_URL

faker = Faker()

print(f"Connection URL: {DB_CONNECTION_URL}")
engine = create_engine(DB_CONNECTION_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(engine)


def generate_all_tables():
    # create and commit 3 groups
    groups = [Group(name=f"Group {i+1}") for i in range(3)]
    session.add_all(groups)
    session.commit()

    # 3-5 teachers
    teachers = [Teacher(name=faker.name()) for _ in range(random.randint(3, 5))]
    session.add_all(teachers)
    session.commit()

    # 30 - 50 students
    students = []
    for _ in range(random.randint(30, 50)):
        student = Student(name=faker.name(), group=random.choice(groups))
        students.append(student)
    session.add_all(students)
    session.commit()

    # 5 - 8 subjects
    subjects = []
    subject_names = [
        "Math",
        "Bio",
        "Chemistry",
        "History",
        "Physics",
        "English",
        "Philosophy",
        "Programming",
    ]

    for name in random.sample(subject_names, random.randint(5, 8)):
        teacher = random.choice(teachers)
        subjects.append(Subject(name=name, teacher=teacher))
    session.add_all(subjects)
    session.commit()

    # generate grades
    grades = []
    for student in students:
        for subject in subjects:
            for _ in range(random.randint(5, 20)):
                grade = Grade(
                    student=student,
                    subject=subject,
                    grade=round(random.uniform(40, 100), 2),
                    date_received=faker.date_between(
                        start_date="-2y", end_date="today"
                    ),
                )
                grades.append(grade)
    session.add_all(grades)
    session.commit()


# generate_all_tables()
