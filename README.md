A simple Python library manager I put together in my spare time to practice backend architecture. It uses SQLModel to handle object-relational mapping (ORM) and hooks into a local SQLite database to track books, students, and loans directly from the terminal.

Project Structure:
├── src/
│   ├── main.py         # Terminal user interface loop & input validation
│   ├── crud.py         # Database operations (Create, Read, Update)
│   ├── models.py       # SQLModel data tables (Book, Student, Loan)
│   └── database.py     # Engine configuration & table initialization
├── requirements.txt    # Third-party dependencies
└── README.md           # You're Here!

Setup in Bash:
git clone https://github.com/peterpitrun-ui/library-manager.git
cd your-repo-name
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python src/main.py
