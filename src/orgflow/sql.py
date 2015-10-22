from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import INTEGER
from sqlalchemy.ext.declarative import declarative_base


MYSQL_CREDS = {
    "proto": "mysql",
    "host": "127.0.0.1",
    "user": "root",
    "pass": "password",
    "name": "orgflow_orgflow"
}

Base = declarative_base()


class Team(Base):
    __tablename__ = 'team'
    id = Column(INTEGER(unsigned=True), primary_key=True)
    name = Column(String(128))


class User(Base):
    __tablename__ = 'user'
    id = Column(INTEGER(unsigned=True), primary_key=True)
    username = Column(String(128))


from sqlalchemy import create_engine
engine = create_engine("{proto}://{user}:{pass}@{host}/{name}".format(**MYSQL_CREDS))

from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)