# library_data.py
# Mock library catalogue and borrower info

from datetime import datetime, timedelta

books = [
    {
        "id": 1,
        "title": "Introduction to Algorithms",
        "author": "Thomas H. Cormen",
        "isbn": "978-0262033848",
        "location": "Floor 2, Section A, Shelf 12",
        "total_copies": 3,
        "available_copies": 1
    },
    {
        "id": 2,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "isbn": "978-0132350884",
        "location": "Floor 1, Section B, Shelf 5",
        "total_copies": 5,
        "available_copies": 5
    },
    {
        "id": 3,
        "title": "Deep Learning",
        "author": "Ian Goodfellow",
        "isbn": "978-0262035613",
        "location": "Floor 3, Section C, Shelf 20",
        "total_copies": 2,
        "available_copies": 0
    },
    {
        "id": 4,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt",
        "isbn": "978-0201616224",
        "location": "Floor 1, Section B, Shelf 8",
        "total_copies": 4,
        "available_copies": 2
    },
    {
        "id": 5,
        "title": "Artificial Intelligence: A Modern Approach",
        "author": "Stuart Russell",
        "isbn": "978-0134610993",
        "location": "Floor 3, Section C, Shelf 18",
        "total_copies": 6,
        "available_copies": 3
    }
]

# Mock user data
# Due dates are generated relative to the current date so the demo stays valid.
user = {
    "name": "Student",
    "borrowed_books": [
        {
            "book_id": 1,
            "due_date": (datetime.now() + timedelta(days=10)).strftime("%Y-%m-%d")
        },
        {
            "book_id": 3,
            "due_date": (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d")
        }
    ],
    "fines": 15.50
}