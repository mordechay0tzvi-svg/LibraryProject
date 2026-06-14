import mysql.connector

class connectionDB:
    def __init__(self):
        self.host="localhost"
        self.port=3306
        self.user='root'
        self.password='library'
        self.database="library_db"

    def get_connection(self):
        """returns a connection to database"""
        return mysql.connector.connect(host=self.host,
                                        port=self.port,
                                        user=self.user,
                                        password=self.password,
                                        database=self.database 
                                        )

    def create_tables(self):
        """create a database name library then uses it to create two table named members and books"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""USE library_db""")
        cursor.execute(
                        """CREATE TABLE IF NOT EXISTS members (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(50) NOT NULL,
                        email VARCHAR(255) UNIQUE NOT NULL,
                        is_active BOOL NOT NULL,
                        total_borrows INT NOT NULL)"""
                        )
        cursor.execute(
                        """CREATE TABLE IF NOT EXISTS books (
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

