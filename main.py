from fastapi import FastAPI
import uvicorn
from routes.reports_routes import app as reports_router
from routes.books_routes import app as books_router
from routes.members_routes import app as members_router

app = FastAPI(title="Library Project API")

app.include_router(reports_router)
app.include_router(books_router)
app.include_router(members_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Library API"}

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)

