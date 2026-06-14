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
    data = data.model_dump()
    new = books.create_book(**data)
    if not new:
        return {"message":"book not created"}
    return {"message":f"book no. {new} created"}







