import datetime
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


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
    users = relationship(
        'User',
        secondary='team_user_link'
    )
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class TeamUserLink(Base):
    __tablename__ = 'team_user_link'
    team_id = Column(
        INTEGER(unsigned=True),
        ForeignKey('team.id'),
        primary_key=True)

    user_id = Column(
        INTEGER(unsigned=True),
        ForeignKey('user.id'),
        primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class User(Base):
    __tablename__ = 'user'
    id = Column(INTEGER(unsigned=True), primary_key=True)
    username = Column(String(128))
    teams = relationship(
        'Team',
        secondary='team_user_link'
    )


from sqlalchemy import create_engine
engine = create_engine("{proto}://{user}:{pass}@{host}/{name}".format(**MYSQL_CREDS))

from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)