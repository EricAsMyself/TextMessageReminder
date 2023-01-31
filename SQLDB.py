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
        
    def close(self):
        self.conn.close()




# class Database():
#   def __init__(self):
#     self.conn = sqlite3.connect('families.db')
#     self.cursor = self.conn.cursor()
#     self.cursor.execute('''
#     CREATE TABLE IF NOT EXISTS `Person` (
#       `Person_id` INT AUTO_INCREMENT PRIMARY KEY,
#       `Fname` VARCHAR(45) NULL,
#       `Lname` VARCHAR(45) NULL,
#       `PhoneNumber` VARCHAR(45) NULL
#     )
#     ''')

#   def add_person(self, first_name, last_name, phone_number):
#     # Insert data
#     # self.cursor.execute(f'''INSERT INTO Person (Fname, Lname, PhoneNumber)
#     #  VALUES ('{first_name}', '{last_name}', '{phone_number}')''')
#      self.cursor.execute(f'''INSERT INTO Person (Fname, Lname, PhoneNumber)
#      VALUES ('Eric', 'Poole', '123')''')
#     # self.conn.commit()

#   def get_people(self):
#     # Query data
#     self.cursor.execute("SELECT * FROM Person")
#     print(self.cursor.fetchall())

#   def close(self):
#     self.conn.commit()
#     self.conn.close()