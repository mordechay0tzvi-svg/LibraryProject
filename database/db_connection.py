import mysql.connector

def get_connection():
    """returns a connection to database"""
    return mysql.connector.connect(host="localhost",
                                   port=3306,
                                   user='root',
                                   database="library",
                                   password='library')

def create_tables():
    """create a database name library then uses it to create two table named members and books"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""CREATE DATABASE IF NOT EXISTS Library""")
    conn.commit()
    cursor.execute("""USE Library""")
    cursor.execute(
                    """CREATE TABLE members (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL,
                    is_active BOOL NOT NULL,
                    total_borrows INT NOT NULL)"""
                    )
    conn.commit()
    cursor.execute(
                    """CREATE TABLE books (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(50) NOT NULL,
                    author VARCHAR(50) NOT NULL,
                    genre ENUM('Fiction', 'Non-Fiction', 'Science', 'History', 'Other') NOT NULL,
                    is_available BOOL NOT NULL,
                    borrowed_by_member_id INT)"""
                    )
    conn.commit()
    cursor.close()
    conn.close()
