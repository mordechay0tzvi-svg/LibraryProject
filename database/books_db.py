from  db_connection import get_connection as connect 
from  db_connection import create_tables as create


class BooksDB:
    def  __init__(self):
        self.host="localhost",
        self.port=3306,
        self.user='root',
        self.database="library",
        self.password='library'
        create()

    def create_book(data:dict) -> int:
        conn = connect()
        cursor = conn.cursor()
        sql = "INSERT INTO books (title, author, genre, is_available, borrowed_by_member_id) VALUES (%s, %s, %s, %s, %s)"
        values = (data['title'], data['author'], data['genre'], True, None)
        cursor.execute(sql, values)
        new_id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        return new_id


    def get_all_books() -> list:
        conn = connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("select * from books")
        all_books = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return all_books

    def get_book_by_id(id:int) -> dict:
        conn = connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("select * from books where id = %s", (id,))
        book = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return book
    
    def update_book(id:int, data:dict) -> int:
        conn = connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE books SET is_available = %s, borrowed_by_member_id = %s WHERE id = %s", (data["is_available"], data["borrowed_by_member_id"], id))
        conn.commit()
        updated = cursor.rowcount
        cursor.close()
        conn.close()
        return updated








        

