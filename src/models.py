from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(autocommit=False, autoflush=False)
Base = declarative_base()


def db_connect(uri):
    engine = create_engine(uri)
    SessionLocal.configure(bind=engine)


def db_disconnect():
    SessionLocal.kw['bind'].dispose()


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200))
    country_name = Column(String(100))