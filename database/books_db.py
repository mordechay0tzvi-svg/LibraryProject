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

    def create_book(data:dict):
        conn = connect()
        cursor = conn.cursor()
        sql = "INSERT INTO books (title, author, genre, is_available, borrowed_by_member_id) VALUES (%s, %s, %s, %s, %s)"
        values = (data['title'], data['author'], data['genre'], True, None)
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()


    def get_all_books():
        conn = connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("select * from books")
        all_books = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return all_books

    def get_book_by_id(id:int):
        conn = connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("select * from books where id = %s", (id))
        book = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return book






        

