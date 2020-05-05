import sqlite3

class Database():

	def __init__(self,db):
		self.conn=sqlite3.connect(db)
		self.cursor=self.conn.cursor()
		self.cursor.execute(""" 
			CREATE TABLE IF NOT EXISTS birthdays (first_name text, last_name text,day_of_birth integer,
			month_of_birth integer,
			year_of_birth integer,
			unique(first_name,last_name) )
			""")


		self.conn.commit()

	def insert(self,fname,lname,day,month,year):
		try:
			self.cursor.execute("""
			INSERT INTO birthdays VALUES (?,?,?,?,?)""",(fname,lname,day,month,year) )
			self.conn.commit()
			return f"Success. Birthday of {fname} has been added successfully"

		except sqlite3.IntegrityError:
			return "Error,You have already added the above person's birthday to BirthdayRetreiver. Please verify."


	def get_records(self,month):
		self.cursor.execute(" SELECT * FROM birthdays where month_of_birth=? ORDER BY day_of_birth ASC",(month,))
		records=self.cursor.fetchall()
		return records






