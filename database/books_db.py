from  db_connection import get_connection as connect 
from  db_connection import create_tables as create


class BooksDB:
    def  __init__(self):
        self.host="localhost"
        self.port=3306
        self.user='root'
        self.database="library"
        self.password='library'
        create()

    def create_book(self, data:dict) -> int:
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


    def get_all_books(self) -> list:
        conn = connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("select * from books")
        all_books = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return all_books


    def get_book_by_id(self, id:int) -> dict:
        conn = connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("select * from books where id = %s", (id,))
        book = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return book
    

    def update_book(self, id:int, data:dict) -> int:
        conn = connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE books SET title = %s, author = %s, genre = %s WHERE id = %s", (data["title"], data["author"], data["genre"], id))
        conn.commit()
        updated = cursor.rowcount
        cursor.close()
        conn.close()
        return updated
    

    def set_available(self, id:int, val:bool, member_id:int):
        conn = connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("UPDATE books SET is_available = %s, borrowed_by_member_id = %s WHERE id = %s", (val, member_id, id))
        conn.commit()
        updated = cursor.rowcount
        cursor.close()
        conn.close()
        return updated


    def count_total_books(self):
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("select count(*) from books")
        conn.commit()
        count = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return count
    

    def count_available_books(self):
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("select count(*) from books where is_available")
        conn.commit()
        count = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return count

    def count_borrowed_books(self):
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("select count(*) from books where is_available = 0")
        conn.commit()
        count = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return count
     
    def count_by_genre(self, genre):
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("select count(*) from books where genre = %s",(genre,))
        conn.commit()
        count = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return count

    def count_active_borrows_by_member(self, member_id):
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("select count(*) from books where member_id = %s",(member_id,))
        conn.commit()
        count = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return count
    
    
    


    







        

