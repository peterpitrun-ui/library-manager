from sqlmodel import Field, SQLModel

class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    author: str
    is_stocked: bool = Field(default=True)

class Student(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    surname: str
    email: str
    phone_number: str


class Loan(SQLModel, table=True):
    loan_id: int | None = Field(default=None, primary_key=True)
    student_id: int = Field(foreign_key="student.id", primary_key=False)
    book_id: int = Field(foreign_key="book.id", primary_key=False)