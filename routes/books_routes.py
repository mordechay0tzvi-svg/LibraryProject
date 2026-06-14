from fastapi import FastAPI, Body, Query, HTTPException
import uvicorn
from pydantic import BaseModel
from database.books_db import BooksDB
from database.members_db import MembersDB
books = BooksDB()
members = MembersDB()
app = FastAPI()

class Book(BaseModel):
    name:str
    author:str
    genre:str

@app.post("/books")
def create_book(data:Book=Body(...)):
    if data.genre not in ["Fiction", 'Non-Fiction', 'Science', 'History',  "Other"]:
        raise HTTPException(status_code=400, detail="not valid genre")
    new = books.create_book(**data.model_dump())
    if not new:
        return {"message":"book not created"}
    return {"message":f"book no. {new} created"}

@app.get("/books")
def all_books():
    return books.get_all_books()

@app.get("/books/{id}")
def book_by_id(id:int):
    book = books.get_book_by_id(id)
    if not book:
        raise HTTPException(status_code=404, detail="book not found")
    return book

@app.put("/books/{id}")
def update_book(id:int, data:Book=Body(...)):
    if data.genre not in ["Fiction", 'Non-Fiction', 'Science', 'History',  "Other"]:
        raise HTTPException(status_code=400, detail="not valid genre")
    updated = books.update_book(id, **data.model_dump())
    if not updated:
        raise HTTPException(status_code=404, detail="book not found")
    return {"message":f"book {id}, updated"}

@app.put("/books/{book_id}/borrow/{member_id}")
def borrow(book_id:int, member_id:int):
    book = books.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="book not found")
    if not book["is_available"]:
        raise HTTPException(status_code=400, detail="book is already borrowed")
    if books.count_active_borrows_by_member(member_id) == 3:
        raise HTTPException(status_code=400, detail="member has reaced maximum borrows")
    borrowed = books.set_available(book_id, False, member_id)
    if not borrowed:
        raise HTTPException(status_code=404, detail="member not found")
    members.increment_borrows(member_id)
    return {"message":f"book {book_id} borrowed"}

@app.put("/books/{book_id}/return/{member_id}")
def return_book(book_id:int, member_id:int):
    book = books.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="book not found")
    if book["member_id"] != member_id:
        raise HTTPException(status_code=400, detail='only borrowed allowed to return book')
    returned = books.set_available(book_id, True, member_id)
    if not returned:
        raise HTTPException(status_code=404, detail="book or member not found")
    return {"message":f"member {member_id} returned book {book_id}"}


    







