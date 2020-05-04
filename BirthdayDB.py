from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3


root=Tk()
root.geometry("600x600")
root.columnconfigure(0, weight=1)   # Set weight to row and 
root.rowconfigure(0, weight=1) 
new_birthday=Toplevel()
new_birthday.geometry("600x600")




display_birthdays=Toplevel()
display_birthdays.geometry("500x500")
display_birthdays.columnconfigure(0, weight=1)   # Set weight to row and 
display_birthdays.rowconfigure(0, weight=1)






root_bgimage=ImageTk.PhotoImage(Image.open("backgroundImages/birthday_bg.png"))
root_bglabel=Label(root, image=root_bgimage)
root_bglabel.place(x=0, y=0, relwidth=1, relheight=1)

addbirthday_bgimage=ImageTk.PhotoImage(Image.open("backgroundImages/addbirthday_bg.png"))
addbirthday_bglabel=Label(new_birthday, image=addbirthday_bgimage)
addbirthday_bglabel.place(x=0, y=0, relwidth=1, relheight=1)

displaybirthdays_bgimage=ImageTk.PhotoImage(Image.open("backgroundImages/dropdown_bg1.png"))
displaybirthdays_bglabel=Label(display_birthdays, image=displaybirthdays_bgimage)
displaybirthdays_bglabel.place(x=0, y=0, relwidth=1, relheight=1)

display_birthdays.withdraw()
dropdown_container=tk.Frame(display_birthdays)
dropdown_container.grid(row=0, column=0)  
dropdown_container.config(bg="#9F5AEA")



add_birthday_container=tk.Frame(new_birthday)
add_birthday_container.config(bg="#005E6E")
new_birthday.withdraw()


first_name=Entry(add_birthday_container,width=15)
last_name=Entry(add_birthday_container,width=15)
day_of_birth=Entry(add_birthday_container,width=15)
month_of_birth=Entry(add_birthday_container,width=15)
year_of_birth=Entry(add_birthday_container,width=15)


style = Style() 
  
# This will be adding style, and  
# naming that style variable as  
# W.Tbutton (TButton is used for ttk.Button). 
  
style.configure('W.TButton', font =
               ('futura', 14, 'bold',), 
                foreground = 'black') 

months={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",
8:"August",9:"September",10:"October",11:"November",12:"December"}
months_dropdown=['January','February','March','April','May','June','July','August','September','October','November','December']


def submit_birthday():
	global first_name
	global last_name
	global day_of_birth
	global month_of_birth
	global year_of_birth

	try:	
		conn=sqlite3.connect('birthday.db')
		cursor=conn.cursor()
		result=cursor.execute(""" INSERT INTO birthdays VALUES (:first_name,:last_name,:day_of_birth,:month_of_birth,:year_of_birth)""",
			{'first_name':first_name.get().upper(),
		 	'last_name':last_name.get().upper(),
		  	'day_of_birth':day_of_birth.get(),
		  	'month_of_birth':month_of_birth.get(),
		  	'year_of_birth':year_of_birth.get()
			} )

		conn.commit()
		conn.close()

		messagebox.showinfo("Success",f"Birthday of {first_name.get()} has been added successfully")

	except sqlite3.IntegrityError:
		messagebox.showerror("Error","You have already added the above person's birthday to BirthdayRetreiver. Please verify.")

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


	# cursor.execute("""
	##		first_name text,
	#		last_name text,
	#		day_of_birth integer,
	#		month_of_birth integer,
	#		year_of_birth integer,
	#		unique(first_name,last_name) )
	#	""") 



	new_birthday.title("Add a new birthday")
	new_birthday.columnconfigure(0, weight=1)   # Set weight to row and 
	new_birthday.rowconfigure(0, weight=1) 

	add_birthday_container.grid(row=0,column=0)

	Label(add_birthday_container,text="First Name",style='W.TButton').grid(row=0,column=0,padx=20,pady=20)
	first_name.grid(row=0,column=1,padx=20,pady=10)

	Label(add_birthday_container,text="Last Name",style='W.TButton').grid(row=1,column=0,padx=20,pady=10)
	last_name.grid(row=1,column=1)

	Label(add_birthday_container,text="Day of Birth",style='W.TButton').grid(row=2,column=0,padx=20,pady=10)
	day_of_birth.grid(row=2,column=1)

	Label(add_birthday_container,text="Month of Birth",style='W.TButton').grid(row=3,column=0,padx=20,pady=10)
	month_of_birth.grid(row=3,column=1)

	Label(add_birthday_container,text="Year of Birth",style='W.TButton').grid(row=4,column=0,padx=20,pady=10)
	year_of_birth.grid(row=4,column=1)

	'''textfield_values=[]
	textfield_values.append(first_name.get())
	textfield_values.append(last_name.get())
	textfield_values.append(day_of_birth.get())
	textfield_values.append(month_of_birth.get())
	textfield_values.append(year_of_birth.get())'''


	submit_btn=Button(add_birthday_container,text="Add Birthday",style='W.TButton',command=submit_birthday)
	submit_btn.grid(row=7,column=1,pady=20)

	quit_btn=Button(add_birthday_container,text="Destroy everthing",style='W.TButton', command=destroy)
	quit_btn.grid(row=8,column=1,pady=20)

	conn.close()

def retrieve_birthday():
	return

def display_birthdays_in_month(dropdown_clicked):
	global display_birthdays
	#birthday_text=""
	#birthday_label=Label(dropdown_container,text=birthday_text,width=50,style='W.TButton')
	#birthday_label.grid(row=1, column=0, columnspan=3, padx=20,pady=10)

	for label in dropdown_container.grid_slaves():
		if int(label.grid_info()["row"]) > 0:
			label.grid_forget()

	
	row=1
	conn=sqlite3.connect('birthday.db')
	cursor=conn.cursor()

	dropdown_month=months_dropdown.index(dropdown_clicked)+1
	print(dropdown_month,"SELECTED DROPDOWN MONTH")
	cursor.execute(" SELECT * FROM birthdays where month_of_birth=? ORDER BY day_of_birth ASC",(dropdown_month,))
	records=cursor.fetchall()

	if(len(records)==0):
		birthday_text="No birthdays found"
		birthday_label=Label(dropdown_container,text=birthday_text,width=40,style='W.TButton')
		birthday_label.grid(row=1, column=0, columnspan=3, padx=20,pady=10)

	else:
		birthday_text=""
		for birthday in records:
			person=f"{birthday[0]} {birthday[1]}:  "
			person_birthday=f"{months[birthday[3]]} {birthday[2]}"
			birthday_text+=person+person_birthday+'\n'

		#birthday_label.grid_forget()	
		birthday_label=Label(dropdown_container,text=birthday_text,width=40,style='W.TButton')
		birthday_label.grid(row=1, column=0, columnspan=3, padx=20,pady=10)

	conn.close()



def retrieve_birthday_by_month():
	# Add a drop down to select the month
	global birthday_month_container
	global display_birthdays
	global months_dropdown

	display_birthdays.deiconify()

	dropdown_clicked=StringVar()
	#dropdown_clicked.set("October")

	dropdown=OptionMenu(dropdown_container,dropdown_clicked,months_dropdown[9],*months_dropdown)
	dropdown.grid(row=0,column=0,columnspan=2,padx=20,pady=20)

	search_btn=Button(dropdown_container,text="Search",style='W.TButton',command=lambda:display_birthdays_in_month(dropdown_clicked.get()))
	search_btn.grid(row=0,column=2,padx=10,pady=10)

	



## First let's make the required UI elements for screen 1 and put them on the screen

main_container = tk.Frame(root)   # bg color to show extent
main_container.grid(row=0, column=0)  
main_container.config(bg="#5B5C5E")   # Grid cell with weight



add_birthday=Button(main_container,text="Add a new Birthday",style='W.TButton',command=add_birthday)
add_birthday.grid(row=0,column=1, columnspan=3,padx=20,pady=10)


retrieve_birthday=Button(main_container,text="Retrieve this week's birthdays",style='W.TButton',command=retrieve_birthday)
retrieve_birthday.grid(row=1,column=1, columnspan=3,padx=20,pady=10)

retrieve_all_birthday=Button(main_container,text="Get all birthdays",style='W.TButton',command=retrieve_birthday_by_month)
retrieve_all_birthday.grid(row=2,column=1, columnspan=3,padx=20,pady=10)

quit_btn=Button(main_container,text="Destroy everthing",style='W.TButton', command=destroy)
quit_btn.grid(row=3,column=1,columnspan=3,padx=20,pady=10)






root.mainloop()
