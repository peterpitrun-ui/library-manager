from sqlmodel import Session, select
from database import engine
from models import Book
from models import Student
from models import Loan

def add_book(title: str, author: str):
    with Session(engine) as session:
        new_book = Book(title=title, author=author)
        session.add(new_book)
        session.commit()
        session.refresh(new_book)
        print(f"Added '{new_book.title}' by {new_book.author} to the database with ID: {new_book.id}")
        return new_book

def add_student(name: str, surname: str, email: str, phone_number: str):
    with Session(engine) as session:
        new_student = Student(name=name, surname=surname, email=email, phone_number=phone_number)
        session.add(new_student)
        session.commit()
        session.refresh(new_student)
        print(f"Added student '{new_student.name} {new_student.surname}' to the database with ID: {new_student.id}")
        return new_student

def get_all_books():
    with Session(engine) as session:
        return session.exec(select(Book)).all()

def get_book_by_id(book_id: int):
    with Session(engine) as session:
        return session.get(Book, book_id)


def create_loan(student_id: int, book_id: int):
    with Session(engine) as session:
        student = session.get(Student, student_id)
        book = session.get(Book, book_id)
        
        if student is None or book is None:
            raise ValueError("Invalid student_id or book_id")
        
        if book.is_stocked == False:
            raise ValueError("This book is already checked out and not in stock!")
        book.is_stocked = False
        new_loan = Loan(student_id=student_id, book_id=book_id)
        session.add(new_loan)
        session.commit()
        session.refresh(new_loan)
        return new_loan

def return_book(book_id: int):
    with Session(engine) as session:
        book = session.get(Book, book_id)
        if book is None:
            raise ValueError("Book not found")
        book.is_stocked = True
        session.commit()
        session.refresh(book)
        return book