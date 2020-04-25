from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from tkinter.ttk import * 
from tkinter import messagebox
import sqlite3


root=Tk()
root.geometry("300x300")
root.columnconfigure(0, weight=1)   # Set weight to row and 
root.rowconfigure(0, weight=1) 
new_birthday=Toplevel()
new_birthday.geometry("400x400")
add_birthday_container=tk.Frame(new_birthday)

new_birthday.withdraw()


first_name=Entry(add_birthday_container,width=20)
last_name=Entry(add_birthday_container,width=20)
day_of_birth=Entry(add_birthday_container,width=20)
month_of_birth=Entry(add_birthday_container,width=20)
year_of_birth=Entry(add_birthday_container,width=20)


style = Style() 
  
# This will be adding style, and  
# naming that style variable as  
# W.Tbutton (TButton is used for ttk.Button). 
  
style.configure('W.TButton', font =
               ('monaco', 14, 'bold',), 
                foreground = 'black') 

def submit_birthday():
	global first_name
	global last_name
	global day_of_birth
	global month_of_birth
	global year_of_birth

	conn=sqlite3.connect('birthday.db')
	cursor=conn.cursor()
	cursor.execute(""" INSERT INTO birthdays VALUES (:first_name,:last_name,:day_of_birth,:month_of_birth,:year_of_birth)""",
		{'first_name':first_name.get(),
		 'last_name':last_name.get(),
		  'day_of_birth':day_of_birth.get(),
		  'month_of_birth':month_of_birth.get(),
		  'year_of_birth':year_of_birth.get()
		} )

	conn.commit()
	conn.close()

	new_birthday.withdraw()

def destroy():
	root.destroy()

def add_birthday():
	global new_birthday
	global add_birthday_container
	global first_name
	global last_name
	global day_of_birth
	global month_of_birth
	global year_of_birth

	new_birthday.deiconify()


	conn=sqlite3.connect('birthday.db')
	cursor=conn.cursor()

	'''cursor.execute("""
		CREATE TABLE birthdays(
			first_name text,
			last_name text,
			day_of_birth integer,
			month_of_birth integer,
			year_of_birth integer)
		""")  '''

	new_birthday.title("Add a new birthday")
	new_birthday.columnconfigure(0, weight=1)   # Set weight to row and 
	new_birthday.rowconfigure(0, weight=1) 

	add_birthday_container.grid(row=0,column=0)

	Label(add_birthday_container,text="First Name").grid(row=0,column=0,padx=20,pady=10)
	first_name.grid(row=0,column=1)

	Label(add_birthday_container,text="Last Name").grid(row=1,column=0,padx=20,pady=10)
	last_name.grid(row=1,column=1)

	Label(add_birthday_container,text="Day of Birth").grid(row=2,column=0,padx=20,pady=10)
	day_of_birth.grid(row=2,column=1)

	Label(add_birthday_container,text="Month of Birth").grid(row=3,column=0,padx=20,pady=10)
	month_of_birth.grid(row=3,column=1)

	Label(add_birthday_container,text="Year of Birth").grid(row=4,column=0,padx=20,pady=10)
	year_of_birth.grid(row=4,column=1)

	'''textfield_values=[]
	textfield_values.append(first_name.get())
	textfield_values.append(last_name.get())
	textfield_values.append(day_of_birth.get())
	textfield_values.append(month_of_birth.get())
	textfield_values.append(year_of_birth.get())'''


	submit_btn=Button(add_birthday_container,text="Add Birthday",command=submit_birthday)
	submit_btn.grid(row=7,column=1,pady=20)

	quit_btn=Button(add_birthday_container,text="Destroy everthing", command=destroy)
	quit_btn.grid(row=8,column=1,pady=20)

	conn.close()

def retrieve_birthday():
	return

def retrieve_all_birthday():
	conn=sqlite3.connect('birthday.db')
	cursor=conn.cursor()

	cursor.execute(" SELECT * FROM birthdays ")
	records=cursor.fetchall()
	print(records)



	conn.close()



## First let's make the required UI elements for screen 1 and put them on the screen

main_container = tk.Frame(root)   # bg color to show extent
main_container.grid(row=0, column=0)     # Grid cell with weight



add_birthday=Button(main_container,text="Add a new Birthday",style='W.TButton',command=add_birthday)
add_birthday.grid(row=0,column=1, columnspan=3,padx=20,pady=10)


retrieve_birthday=Button(main_container,text="Retrieve this week's birthdays",style='W.TButton',command=retrieve_birthday)
retrieve_birthday.grid(row=1,column=1, columnspan=3,padx=20,pady=10)

retrieve_all_birthday=Button(main_container,text="Get all birthdays",style='W.TButton',command=retrieve_all_birthday)
retrieve_all_birthday.grid(row=2,column=1, columnspan=3,padx=20,pady=10)

quit_btn=Button(main_container,text="Destroy everthing",style='W.TButton', command=destroy)
quit_btn.grid(row=3,column=1,columnspan=3,padx=20,pady=10)






root.mainloop()
