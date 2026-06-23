from database import create_db_and_tables
import crud

def main():
    print("Telling the engine to build our tables...")
    create_db_and_tables()
    print("Tables successfully generated!")

    while True:
        print("Select an option:")
        print("Option 1: Add a Book")
        print("Option 2: Add a Student")
        print("Option 3: List all Books")
        print("Option 4: Borrow a Book")
        print("Option 5: Return a Book")
        print("Option 6: Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            crud.add_book(title, author)
        elif choice == "2":
            name = input("Enter the student's name: ")
            surname = input("Enter the student's surname: ")
            email = input("Enter the student's email: ")
            phone_number = input("Enter the student's phone number: ")
            crud.add_student(name, surname, email, phone_number)
        elif choice == "3":
            books = crud.get_all_books()
            for book in books:
                print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, In Stock: {book.is_stocked}")
        elif choice == "4":
            student_id = input("Enter the student ID: ")
            book_id = input("Enter the book ID: ")
            try:
                student_id = int(student_id)
                book_id = int(book_id)
                loan = crud.create_loan(student_id, book_id)
                print(f"Loan created with ID: {loan.loan_id}")
            except ValueError as e:
                print(e)
        elif choice == "5":
            book_id = input("Enter the book ID: ")
            try:
                book_id = int(book_id)
                crud.return_book(book_id)
                print("Book returned successfully.")
            except ValueError as e:
                print(e)
        elif choice == "6":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
    