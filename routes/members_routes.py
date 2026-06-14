from fastapi import FastAPI, Body, Query, HTTPException
import uvicorn
from pydantic import BaseModel
from database.books_db import BooksDB
from database.members_db import MembersDB
books = BooksDB()
members = MembersDB()
app = FastAPI()

class Member(BaseModel):
    name:str
    email:str

@app.post("/members")
def add_member(data:Member=Body(...)):
    new = members.create_member(**data.model_dump())
    if not new:
        return {"message":"member not added"}
    return {"message":f"member no. {new} added"}

