from sqlalchemy import create_engine, Column, String, Integer, text, select
from sqlalchemy.orm import declarative_base, sessionmaker
from config import config
from models.models import (
    Student,
    Teacher,
    Grade,
    Subject,
    Group,
)


# get all config data and serialize it to correct URL
username = config.get("DB", "user")
password = config.get("DB", "password")
db_name = config.get("DB", "db_name")
domain = config.get("DB", "domain")
port = config.get("DB", "db_port")

DB_CONNECTION_URL = f"postgresql://{username}:{password}@{domain}:{port}/{db_name}"
print(DB_CONNECTION_URL)


engine = create_engine(DB_CONNECTION_URL)
DBSession = sessionmaker(bind=engine)
db_session = DBSession()

# test DB
# print(db_session.query(text("1 + 1")).one())


# Base = declarative_base()
# Base.metadata.create_all(engine)


# db_session.add_all(students)
# db_session.commit()
print(db_session.execute(select(Teacher)).all())
