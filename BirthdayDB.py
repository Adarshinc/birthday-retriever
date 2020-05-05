from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk,Image
from tkinter import messagebox
from db import Database

  
# This will be adding style, and  
# naming that style variable as  
# W.Tbutton (TButton is used for ttk.Button). 
  


months={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",
8:"August",9:"September",10:"October",11:"November",12:"December"}

months_dropdown=['January','February','March','April','May','June','July','August','September','October','November','December']



def main():
	program=MainScreen()
	program.window.mainloop()




class MainScreen():

	# Declaring the constructor of the class
	def __init__(self):
		self.window=tk.Tk()
		self.set_window_properties()


	def set_window_properties(self):
		self.window.geometry("600x600")
		self.window.columnconfigure(0, weight=1)   # Set weight to row and 
		self.window.rowconfigure(0, weight=1) 
		self.window.minsize(600,600)
		self.window.maxsize(600,600)

		self.set_window_background()

	def set_window_background(self):
		window_bgimage=ImageTk.PhotoImage(Image.open("backgroundImages/birthday_bg.png"))
		window_bglabel=Label(self.window, image=window_bgimage)
		window_bglabel.image=window_bgimage
		window_bglabel.place(x=0, y=0, relwidth=1, relheight=1)
		self.create_widgets()


	def create_widgets(self):
		ttk.Style().configure('W.TButton', font =
               ('futura', 14, 'bold',), 
                foreground = 'black') 

		frame = tk.Frame(self.window)   # bg color to show extent
		frame.grid(row=0, column=0)  
		frame.config(bg="#5B5C5E")   # Grid cell with weight

		add_birthday=Button(frame,text="Add a new Birthday",style='W.TButton',command=lambda:AddBirthdayScreen())
		add_birthday.grid(row=0,column=1, columnspan=3,padx=20,pady=10)

		retrieve_birthday=Button(frame,text="Retrieve this week's birthdays",style='W.TButton')#,command=retrieve_birthday)
		retrieve_birthday.grid(row=1,column=1, columnspan=3,padx=20,pady=10)

		retrieve_all_birthday=Button(frame,text="Get all birthdays",style='W.TButton',command=lambda:ViewBirthdayScreen())
		retrieve_all_birthday.grid(row=2,column=1, columnspan=3,padx=20,pady=10)

		quit_btn=Button(frame,text="Destroy everthing",style='W.TButton')#, command=root.destroy)
		quit_btn.grid(row=3,column=1,columnspan=3,padx=20,pady=10)

class AddBirthdayScreen():
	def __init__(self):
		self.window=Toplevel()
		#self.frame=None
		self.first_name=None
		self.last_name=None
		self.day_of_birth=None
		self.month_of_birth=None
		self.year_of_birth=None
		self.set_window_properties()


	def set_window_properties(self):
		self.window.geometry("600x600")
		self.window.columnconfigure(0, weight=1)   # Set weight to row and 
		self.window.rowconfigure(0, weight=1) 
		self.window.minsize(600,600)
		self.window.maxsize(600,600)
		self.set_window_background()

	def set_window_background(self):
		window_bgimage=ImageTk.PhotoImage(Image.open("backgroundImages/addbirthday_bg.png"))
		window_bglabel=Label(self.window, image=window_bgimage)
		window_bglabel.image=window_bgimage
		window_bglabel.place(x=0, y=0, relwidth=1, relheight=1)
		self.create_widgets()

	def add_birthday(self):
		fname=self.first_name.get().upper()
		lname=self.last_name.get().upper()
		day=self.day_of_birth.get()
		month=self.month_of_birth.get()
		year=self.year_of_birth.get()

		db=Database('birthday.db')
		result_text=db.insert(fname,lname,day,month,year)


		messagebox.showinfo("Result",result_text)


	def create_widgets(self):
		ttk.Style().configure('W.TButton', font =
               ('futura', 14, 'bold',), 
                foreground = 'black')

		frame = tk.Frame(self.window)   # bg color to show extent
		frame.grid(row=0, column=0)  
		frame.config(bg="#005E6E")   # Grid cell with weight

		Label(frame,text="First Name",style='W.TButton').grid(row=0,column=0,padx=20,pady=20)
		self.first_name=Entry(frame,width=15)
		self.first_name.grid(row=0,column=1,padx=20,pady=10)

		Label(frame,text="Last Name",style='W.TButton').grid(row=1,column=0,padx=20,pady=20)
		self.last_name=Entry(frame,width=15)
		self.last_name.grid(row=1,column=1,padx=20,pady=10)

		Label(frame,text="Day of Birth",style='W.TButton').grid(row=2,column=0,padx=20,pady=20)
		self.day_of_birth=Entry(frame,width=15)
		self.day_of_birth.grid(row=2,column=1,padx=20,pady=10)

		Label(frame,text="Month of birth",style='W.TButton').grid(row=3,column=0,padx=20,pady=20)
		self.month_of_birth=Entry(frame,width=15)
		self.month_of_birth.grid(row=3,column=1,padx=20,pady=10)

		Label(frame,text="Year of birth",style='W.TButton').grid(row=4,column=0,padx=20,pady=20)
		self.year_of_birth=Entry(frame,width=15)
		self.year_of_birth.grid(row=4,column=1,padx=20,pady=10)

		submit_btn=Button(frame,text="Add Birthday",style='W.TButton',command=lambda:self.add_birthday())  
		submit_btn.grid(row=5,column=1,pady=20)

		quit_btn=Button(frame,text="Destroy everthing",style='W.TButton', command=self.window.destroy)
		quit_btn.grid(row=6,column=1,pady=20)


class ViewBirthdayScreen():

	def __init__(self):
		self.window=Toplevel()
		self.frame=None
		self.dropdown_clicked=StringVar()
		self.set_window_properties()


	def set_window_properties(self):
		self.window.geometry("600x600")
		self.window.columnconfigure(0, weight=1)   # Set weight to row and 
		self.window.rowconfigure(0, weight=1) 
		self.window.minsize(600,600)
		self.window.maxsize(600,600)
		self.set_window_background()

	def set_window_background(self):
		window_bgimage=ImageTk.PhotoImage(Image.open("backgroundImages/dropdown_bg1.png"))
		window_bglabel=Label(self.window, image=window_bgimage)
		window_bglabel.image=window_bgimage
		window_bglabel.place(x=0, y=0, relwidth=1, relheight=1)
		self.create_widgets()

	def display_birthday(self):
		selected_month=self.dropdown_clicked.get()
		dropdown_month=months_dropdown.index(selected_month)+1

		for label in self.frame.grid_slaves():
			if int(label.grid_info()["row"]) > 0:
				label.grid_forget()

		# Call instance method of database class to retreive records and store in a variable records
		db=Database('birthday.db')
		records=db.get_records(dropdown_month)
		# records=database.retrieveByMonth() etc

		if(len(records)==0):
			birthday_text="No birthdays found"
			birthday_label=Label(self.frame,text=birthday_text,width=40,style='W.TButton')
			birthday_label.grid(row=1, column=0, columnspan=3, padx=20,pady=10)

		else:
			birthday_text=""
			for birthday in records:
				person=f"{birthday[0]} {birthday[1]}:  "
				person_birthday=f"{months[birthday[3]]} {birthday[2]}"
				birthday_text+=person+person_birthday+'\n'

			#birthday_label.grid_forget()	
			birthday_label=Label(self.frame,text=birthday_text,width=40,style='W.TButton')
			birthday_label.grid(row=1, column=0, columnspan=3, padx=20,pady=10)


	def create_widgets(self):
		ttk.Style().configure('W.TButton', font =
               ('futura', 14, 'bold',), 
                foreground = 'black')

		self.frame = tk.Frame(self.window)   # bg color to show extent
		self.frame.grid(row=0, column=0)  
		self.frame.config(bg="#9F5AEA") 

		dropdown=OptionMenu(self.frame,self.dropdown_clicked,months_dropdown[9],*months_dropdown)
		dropdown.grid(row=0,column=0,columnspan=2,padx=20,pady=20)

		search_btn=Button(self.frame,text="Search",style='W.TButton',command=lambda:self.display_birthday())
		search_btn.grid(row=0,column=2,padx=10,pady=10)




if __name__ == "__main__":
    main()
		