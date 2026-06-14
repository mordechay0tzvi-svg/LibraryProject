from fastapi import FastAPI, Body, Query, HTTPException
import uvicorn
from pydantic import BaseModel
from database.books_db import BooksDB
books = BooksDB()
app = FastAPI()

class Book(BaseModel):
    name:str
    author:str
    genre:str

@app.post("/books")
def create_book(data:Book=Body(...)):
    if data["genre"] not in ["Fiction", 'Non-Fiction', 'Science', 'History',  "Other"]:
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

@app.put("books/{id}")
def update_book(id:int, data:Book=Body(...)):
    if data["genre"] not in ["Fiction", 'Non-Fiction', 'Science', 'History',  "Other"]:
        raise HTTPException(status_code=400, detail="not valid genre")
    updated = books.update_book(id, **data.model_dump())
    if not updated:
        raise HTTPException(status_code=404, detail="book not found")
    return {"message":f"book {id}, updated"}









