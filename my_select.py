from sqlalchemy import func, desc

from models.models import Student, Grade, Subject, Group, Teacher
from db import db_session


def select_1():
    return (
        db_session.query(Student.name, func.avg(Grade.grade).label("avg_grade"))
        .join(Grade)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )


def select_2(subject: str = "Math"):

    subject = db_session.query(Subject).where(Subject.name.like(subject)).first()
    if not subject:
        return "subject not found"
    return (
        db_session.query(
            Student.id, Student.name, func.avg(Grade.grade).label("avg_grade")
        )
        .join(Grade, Grade.student_id == Student.id)
        .filter(Grade.subject_id == subject.id)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .first()
    ) or None


def select_3(subject: str = "Math"):
    subject = db_session.query(Subject).where(Subject.name.like(subject)).first()
    if not subject:
        return "subject not found"
    return (
        db_session.query(
            Group.id,
            Group.name,
            func.avg(Grade.grade).label("avg_grade"),
        )
        .join(Student, Student.group_id == Group.id)
        .join(Grade, Grade.student_id == Student.id)
        .filter(Grade.subject_id == subject.id)
        .group_by(Group.id, Group.name)
        .all()
    ) or None


def select_4():
    return db_session.query(func.avg(Grade.grade).label("avg_grade")).all()


def select_5(teacher_name: str = "Mr. Eugene Graham"):
    teacher = db_session.query(Teacher.id).where(Teacher.name == teacher_name).first()
    if not teacher:
        return "teacher not found"
    return db_session.query(Subject.name).where(Subject.teacher_id == teacher.id).all()


def select_6(group_name: str = "Group 1"):
    group = db_session.query(Group.id).where(Group.name == group_name).first()
    if not group:
        return "Provided group not found"
    return db_session.query(Student.name).where(Student.group_id == group.id).all()


def select_7(group_name: str = "Group 1", subject: str = "Math"):
    group = db_session.query(Group.id).where(Group.name == group_name).first()
    subject = db_session.query(Subject.id).where(Subject.name.like(subject)).first()
    if not subject or not group:
        return "subject or group not found"
    return (
        db_session.query(Student.name, Grade.grade)
        .join(Grade, Grade.student_id == Student.id)
        .where(Student.group_id == group.id)
        .where(Grade.subject_id == subject.id)
        .all()
    )


def select_8(teacher_name: str = "Mr. Eugene Graham"):
    try:
        result = (
            db_session.query(func.avg(Grade.grade).label("avg_grade"))
            .join(Subject, Grade.subject_id == Subject.id)
            .filter(Subject.teacher_id == Teacher.id)
            .filter(Teacher.name == teacher_name)
            .scalar()
        )

        if not result:
            return "no grades found for this teacher"

        return round(float(result), 2)

    except Exception as e:
        return f"error: {str(e)}"


def select_9(student_name: str):
    try:
        results = (
            db_session.query(Subject.name)
            .join(Grade, Grade.subject_id == Subject.id)
            .join(Student, Student.id == Grade.student_id)
            .filter(Student.name == student_name)
            .distinct()
            .all()
        )

        if not results:
            return "no courses found for this student"

        return [result[0] for result in results]

    except Exception as e:
        return f"error: {str(e)}"


def select_10(student_name: str, teacher_name: str):
    try:
        results = (
            db_session.query(Subject.name)
            .join(Grade, Grade.subject_id == Subject.id)
            .join(Student, Student.id == Grade.student_id)
            .join(Teacher, Teacher.id == Subject.teacher_id)
            .filter(Student.name == student_name, Teacher.name == teacher_name)
            .distinct()
            .all()
        )

        if not results:
            return "no courses found for this student and teacher combination"

        return [result[0] for result in results]

    except Exception as e:
        return f"error: {str(e)}"


if __name__ == "__main__":
    print(select_1())
