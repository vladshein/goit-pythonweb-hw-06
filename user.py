from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from faker import Faker

fake = Faker()

engine = create_engine("sqlite:///users.db")  # update to correct postrges one
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120))
    age = Column(Integer)
    email = Column(String(120))

    # __table_args__ = (CheckConstraint(),)


Base.metadata.create_all(engine)
# new_student = Student(name="Steve", age=20, email="steve@example.com")
students: list = []

for i in range(50):
    student = Student(
        name=fake.name(), age=fake.random_int(min=16, max=30), email=fake.email()
    )
    students.append(student)
    print(f"i is {i}")

session.add_all(students)
session.commit()
