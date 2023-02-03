import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("families.db")
        self.cursor = self.conn.cursor()
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS people (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fname TEXT NOT NULL,
                lname TEXT NOT NULL,
                phone INTEGER NOT NULL
            )
        """)
        
    def add_person(self, fname, lname, phone_num):
        self.cursor.execute(f"""
            INSERT INTO people (fname, lname, phone)
            VALUES ('{fname}','{lname}','{phone_num}')
        """)
        self.conn.commit()
        
    def remove_person(self, name):
        self.cursor.execute("""
            DELETE FROM people
            WHERE name = ?
        """, (name,))
        self.conn.commit()
        
    def get_people(self):
        self.cursor.execute("SELECT * FROM people")
        return self.cursor.fetchall()

    def check_person(self, fname, lname):
        self.cursor.execute(f"SELECT fname, lname FROM people Where fname = '{fname}' AND lname = '{lname}'")
        return False if not self.cursor.fetchall() else True # returns True if person is found

    def close(self):
        self.conn.close()

