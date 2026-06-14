from fastapi import APIRouter, Body, Query, HTTPException
import uvicorn
from pydantic import BaseModel
from database.books_db import BooksDB
from database.members_db import MembersDB
books = BooksDB()
members = MembersDB()
app = APIRouter()

class Member(BaseModel):
    name:str
    email:str

@app.post("/members")
def add_member(data:Member=Body(...)):
    new = members.create_member(data.model_dump())
    if not new:
        return {"message":"member not added"}
    return {"message":f"member no. {new} added"}

@app.get("/members")
def all_members():
    return members.get_all_members()

@app.get("/members/{id}")
def id_member(id:int):
    member = members.get_member_by_id(id)
    if not member:
        raise HTTPException(status_code=404, detail="book not found")
    return member

@app.put("/members/{id}")
def update_member(id:int, data:Member=Body(...)):
    member = members.update_member(id, data.model_dump())
    if not member:
        raise HTTPException(404, "member not found")
    return {"message":f"member {id} updated"}

@app.put("/members/{id}/deactivate")
def deactivate_member(id:int):
    changed = members.deactivate_member(id)
    if not changed:
        raise HTTPException(404, "member not found")
    return {"message":f"member {id} deactivate"}

@app.put("/members/{id}/activate")
def activate_member(id:int):
    changed = members.activate_member(id)
    if not changed:
        raise HTTPException(404, "member not found")
    return {"message":f"member {id} activate"}

