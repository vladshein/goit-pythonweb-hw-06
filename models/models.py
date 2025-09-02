from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


# Students table
class Student(Base):
    __tablename__ = "students"

    def __repr__(self):
        return f"#{self.id}: {self.name}"

    def __str__(self):
        return f"#{self.id}: {self.name}"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120), nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id"))

    group = relationship("Group", back_populates="students")
    grades = relationship("Grade", back_populates="student")


# Teachers table
class Teacher(Base):
    __tablename__ = "teachers"

    def __repr__(self):
        return f"#{self.id}: {self.name}"

    def __str__(self):
        return f"#{self.id}: {self.name}"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120), nullable=False)

    subjects = relationship("Subject", back_populates="teacher")


# Groups table
class Group(Base):
    __tablename__ = "groups"

    def __repr__(self):
        return f"#{self.id}: {self.name}"

    def __str__(self):
        return f"#{self.id}: {self.name}"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120), nullable=False)

    students = relationship("Student", back_populates="group")


# Subjects table
class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))

    teacher = relationship("Teacher", back_populates="subjects")
    grades = relationship("Grade", back_populates="subject")


# Grades table
class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    grade = Column(Float, nullable=False)
    date_received = Column(Date, nullable=False)

    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")
