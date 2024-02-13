from contextvars import ContextVar

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class ContextWrapper:
    def __init__(self, var: ContextVar):
        self.var = var

    def __getattr__(self, item):
        _var = self.var.get()
        return getattr(_var, item)


SessionLocal = sessionmaker(autocommit=False, autoflush=False)
Base = declarative_base()
session_var = ContextVar("session")
db_session = ContextWrapper(session_var)


def db_connect(uri):
    engine = create_engine(uri)
    SessionLocal.configure(bind=engine)


def db_disconnect():
    SessionLocal.kw["bind"].dispose()


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200))
    country_name = Column(String(100))
