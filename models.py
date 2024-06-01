from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, Date, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

engine = create_engine("sqlite:///library.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Books(Base):
    __tablename__ = "table_books"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(Date, nullable=False)
    author_id = Column(Integer, nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Authors(Base):
    __tablename__ = 'table_authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)


class Students(Base):
    __tablename__ = 'table_students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def get_students_with_true_scholarship(cls):
        return session.query(Students).filter(Students.scholarship == True).all()

    @classmethod
    def get_students_with_by_average_score(cls, average_score: float):
        return session.query(Students).filter(Students.average_score > average_score).all()


class ReceivingBooks(Base):
    __tablename__ = 'table_receiving_books'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    date_of_issue = Column(DateTime, nullable=False, default=datetime.now())
    date_of_return = Column(DateTime)

    @hybrid_property
    def count_date_with_book(self):
        if self.date_of_return:
            return self.date_of_return - self.date_of_issue
        return datetime.now() - self.date_of_issue

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}