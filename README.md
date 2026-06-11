# LibraryProject
"""LibraryProject"""
Manages the library using a books database and members database.

This project is a library management system that allows managing books and members. Users can add books, register members, borrow and return books, and view reports.

libraryProject/
│
│
├── main.py
├── database/
│ ├── db_connection.py
│ ├── book_db.py
│ └── member_db.py
├── routes/
│ ├── book_routes.py
│ ├── member_routes.py
│ └── report_routes.py
├── logs/
│ └── app.log
│
├── README.md
├── requirements.txt
└── .gitignore

Books Table
| Field                 | Description                                                          |
| --------------------- | -------------------------------------------------------------------- |
| id                    | Primary key                                                          |
| title                 | Book title, required field, up to 50 characters                      |
| author                | Author name, required field, up to 50 characters                     |
| genre                 | Book genre (ENUM): Fiction / Non-Fiction / Science / History / Other |
| available_is          | Whether the book is available for borrowing (FALSE = borrowed)       |
| id_member_by_borrowed | ID of the member currently borrowing the book (NULL if available)    |

Members Table
| Field         | Description                                          |
| ------------- | ---------------------------------------------------- |
| id            | Primary key                                          |
| name          | Member name, required field, up to 50 characters     |
| email         | Unique email address, required field                 |
| active_is     | Whether the member is active (FALSE = cannot borrow) |
| borrows_total | Total number of borrows made by the member           |

System Functions
| Function       | Description                                                                       |
| -------------- | --------------------------------------------------------------------------------- |
| connection_get | Creates a MySQL connection for all classes                                        |
| tables_create  | Creates `books` and `members` tables if they don't exist (runs on server startup) |

Books manager object methods
| Method                                    | Description                                                   |
| ----------------------------------------- | ------------------------------------------------------------- |
| create_book(data)                         | Create a new book (default: available=True, borrowed_by=NULL) |
| get_all_books()                           | Retrieve all books                                            |
| get_book_by_id(id)                        | Retrieve a book by ID                                         |
| update_book(id, data)                     | Update book fields                                            |
| set_available(id, val, member_id)         | Update availability and borrow/return status                  |
| count_books_total()                       | Total number of books in the system                           |
| count_available_books()                   | Number of available books                                     |
| count_borrowed_books()                    | Number of borrowed books                                      |
| count_by_genre(genre)                     | Count books by genre                                          |
| count_active_borrows_by_member(member_id) | Number of books currently borrowed by a member                |

Members manager object methods
| Method                  | Description                                        |
| ----------------------- | -------------------------------------------------- |
| create_member(data)     | Create a new member (active=True, borrows_total=0) |
| get_all_members()       | Retrieve all members                               |
| get_member_by_id(id)    | Retrieve member by ID                              |
| update_member(id, data) | Update member fields                               |
| deactivate_member(id)   | Deactivate a member                                |
| activate_member(id)     | Activate a member                                  |
| increment_borrows(id)   | Increase borrow counter by 1                       |
| count_active_members()  | Count active members                               |
| get_top_member()        | Member with the highest number of borrows          |

# 📚 Library Management API (Base URL: http://localhost:8000)

| Module   | Method | Endpoint                                  | Description |
|----------|--------|-------------------------------------------|-------------|
| Books    | POST   | http://localhost:8000/books/              | Create a new book |
| Books    | GET    | http://localhost:8000/books/              | Get all books |
| Books    | GET    | http://localhost:8000/books/{id}          | Get book by ID |
| Books    | PUT    | http://localhost:8000/books/{id}          | Update book details |
| Books    | PUT    | http://localhost:8000/books/{id}/borrow/{member_id} | Borrow a book by member |
| Books    | PUT    | http://localhost:8000/books/{id}/return/{member_id} | Return a book by member |

| Module   | Method | Endpoint                                  | Description |
|----------|--------|-------------------------------------------|-------------|
| Members  | POST   | http://localhost:8000/members/            | Create a new member |
| Members  | GET    | http://localhost:8000/members/            | Get all members |
| Members  | GET    | http://localhost:8000/members/{id}        | Get member by ID |
| Members  | PUT    | http://localhost:8000/members/{id}        | Update member details |
| Members  | PUT    | http://localhost:8000/members/{id}/deactivate | Deactivate member |
| Members  | PUT    | http://localhost:8000/members/{id}/activate   | Activate member |

| Module   | Method | Endpoint                                  | Description |
|----------|--------|-------------------------------------------|-------------|
| Reports  | GET    | http://localhost:8000/reports/summary     | General system summary report |
| Reports  | GET    | http://localhost:8000/reports/books-by-genre | Books grouped by genre |
| Reports  | GET    | http://localhost:8000/reports/top-member  | Most active borrowing member |






"""CREATE DATABASE IF NOT EXISTS Library"""

"""CREATE TABLE members (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50) NOT NULL,
email VARCHAR(255) UNIQUE,
is_active BOOL NOT NULL,
total_borrows INT NOT NULL)"""

"""CREATE TABLE books (
id INT AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(50) NOT NULL,
author VARCHAR(50) NOT NULL,
genre ENUM('Fiction', 'Non-Fiction', 'Science', 'History', 'Other') NOT NULL,
is_available BOOL NOT NULL,
borrowed_by_member_id INT)"""



