#!/usr/bin/env python3.4
import orgflow.sql

MYSQL_CREDS = {
    "proto": "mysql",
    "host": "127.0.0.1",
    "user": "root",
    "pass": "password",
    "name": "orgflow_orgflow"
}

from sqlalchemy import create_engine
engine = create_engine("{proto}://{user}:{pass}@{host}/{name}".format(**MYSQL_CREDS))

from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
orgflow.sql.Base.metadata.create_all(engine)