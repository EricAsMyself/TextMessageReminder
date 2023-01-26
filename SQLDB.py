import sqlite3







class Database():
  def __init__(self):
    conn = sqlite3.connect('families.db')
    self.cursor = conn.cursor()
    self.cursor.execute('''
    CREATE TABLE IF NOT EXISTS `Person` (
      `Person_id` INT AUTO_INCREMENT PRIMARY KEY,
      `Fname` VARCHAR(45) NULL,
      `Lname` VARCHAR(45) NULL,
      `PhoneNumber` VARCHAR(45) NULL
    )
    ''')
  def add_person(self):
    # Insert data
    self.cursor.execute("INSERT INTO Person (Fname, Lname, PhoneNumber) VALUES ('Eric', 'Poole', '+15037268721')")

  def get_people(self):
    # Query data
    return self.cursor.execute("SELECT * FROM Person")

  def close(self):
    self.conn.commit()
    self.conn.close()