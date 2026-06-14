from fastapi import FastAPI, Body, Query, HTTPException
import uvicorn
from pydantic import BaseModel
from database.books_db import BooksDB
from database.members_db import MembersDB
books = BooksDB()
members = MembersDB()
app = FastAPI()

@app.get("/reports/summary")
def summary():
    return {"total books":books.count_total_books(),
            "unavailable books":books.count_borrowed_books(),
            "available books":books.count_available_books()}

@app.get("/reports/books-by-genre")
def genres():
    return books.count_by_genre()

@app.get("/reports/top-member")
def top_member():
    return members.get_top_member()


