from tkinter import *
from program import Program
import pyperclip
root = Tk()
passwlocker=Program()

class WelcomeFrame(Frame):
	def __init__(self, master):
		master.title("Passlocker 1.0")
		Frame.__init__(self, master,width=12)
		self.default()
	def default(self):
		self.welcomescreen = Frame()
		self.welcome =Label(self.welcomescreen,text="Welcome to \nPasslocker 1.0",font=("Calibri", 44))
		self.loginbutton = Button(self.welcomescreen,text="Login",command=self.login)
		self.userbutton = Button(self.welcomescreen,text="Add User",command=self.adduser)
		self.welcome.grid(row=0,columnspan=2)
		self.loginbutton.grid(row=1,column=0)
		self.userbutton.grid(row=1,column=1)
		self.welcomescreen.grid()
	def login(self):
		self.welcomescreen.destroy()
		self.loginscreen=Frame()
		Label(self.loginscreen, text="Username: ",font=("Calibri",20)).grid(row=0,column=0,columnspan=6)
		Label(self.loginscreen, text="Password: ",font=("Calibri",20)).grid(row=1, column=0, columnspan=6)
		Button(self.loginscreen, text="Login",font=("Calibri",20),command=self.dologin).grid(row=2, column=3, columnspan=6)
		self.unameentry=Entry(self.loginscreen,fg='#dddddd')
		self.passentry = Entry(self.loginscreen,show="*",fg='#dddddd')
		self.unameentry.grid(row=0,column=6,columnspan=6)
		self.passentry.grid(row=1,column=6,columnspan=6)
		self.loginscreen.grid()
	def adduser(self):
		self.welcomescreen.destroy()
		self.createscreen=Frame()
		Label(self.createscreen, text="Username: ", font=("Calibri", 20)).grid(row=0, column=0, columnspan=6)
		Label(self.createscreen, text="Password: ", font=("Calibri", 20)).grid(row=1, column=0, columnspan=6)
		Button(self.createscreen, text="Add User", font=("Calibri", 20), command=self.dologin).grid(row=2, column=3,columnspan=6)
		self.unameentry = Entry(self.createscreen, fg='#dddddd')
		self.passentry = Entry(self.createscreen, show="*", fg='#dddddd')
		self.unameentry.grid(row=0, column=6, columnspan=6)
		self.passentry.grid(row=1, column=6, columnspan=6)
		self.createscreen.grid()
	def showpass(self):
		self.managescreen.destroy()
		self.showscreen=Frame(width=12)
		Label(self.showscreen, text="Name", borderwidth=1, font=("Calibri", 20), relief="ridge").grid(row=0, column=0, columnspan=3)
		Label(self.showscreen, text="User", borderwidth=1, font=("Calibri", 20), relief="ridge").grid(row=0, column=3, columnspan=3)
		Label(self.showscreen, text="Pass", borderwidth=1, font=("Calibri", 20), relief="ridge").grid(row=0, column=6, columnspan=3)
		index=1
		for cred in self.userobject.show():
			Label(self.showscreen, text=cred[0], borderwidth=1, font=("Calibri", 20), relief="ridge").grid(row=index, column=0, columnspan=3)
			Label(self.showscreen, text=cred[1], borderwidth=1, font=("Calibri", 20), relief="ridge").grid(row=index, column=3, columnspan=3)
			Label(self.showscreen, text=cred[2], borderwidth=1, font=("Calibri", 20), relief="ridge").grid(row=index, column=6, columnspan=3)
			Button(self.showscreen, text="copy",borderwidth=1, font=("Calibri", 20), relief="ridge",command=lambda: pyperclip.copy(cred[2])).grid(row=index,column=9,columnspan=3)
			index+=1
		self.showscreen.grid()
	def addcreds(self):
		self.managescreen.destroy()
		self.addscreen=Frame(width=12)
		Label(self.addscreen, text="Name: ",font=("Calibri",20)).grid(row=0,column=0,columnspan=6)
		Label(self.addscreen, text="User: ",font=("Calibri",20)).grid(row=1, column=0, columnspan=6)
		Label(self.addscreen, text="Pass: ",font=("Calibri",20)).grid(row=2, column=0, columnspan=6)
		Button(self.addscreen, text="Save Cred",font=("Calibri",20),command=self.savecred).grid(row=2, column=3, columnspan=6)
		self.unameentry=Entry(self.addscreen,fg='#dddddd')
		self.userentry=Entry(self.addscreen,fg='#dddddd')
		self.passentry = Entry(self.addscreen,show="*",fg='#dddddd')
		self.unameentry.grid(row=0,column=6,columnspan=6)
		self.userentry.grid(row=1,column=6,columnspan=6)
		self.passentry.grid(row=1,column=6,columnspan=6)
		self.addscreen.grid()
	def changekey(self):
		pass
	def successlogin(self):
		self.loginscreen.destroy()
		self.managescreen=Frame()
		Label(self.managescreen,text=f"Welcome back {self.userobject.name}",font=("Calibri", 25)).grid(row=0,column=0,columnspan=12)
		Button(self.managescreen, text="Show credentials", font=("Calibri", 20), command=self.showpass).grid(row=1, column=0,columnspan=10)
		Button(self.managescreen, text="Add credential", font=("Calibri", 20), command=self.addcreds).grid(row=2, column=0,columnspan=10)
		Button(self.managescreen, text="Change Master pass", font=("Calibri", 20), command=self.changekey).grid(row=3, column=0,columnspan=10)
		self.managescreen.grid()
	def errorlogin(self):
		self.unameentry.delete(0,END)
		self.passentry.delete(0, END)
		messagebox.showerror("Failed to Login","Wrong password!")
	#Interactive methods -->
	def dologin(self):
		username=self.unameentry.get()
		password=self.passentry.get()
		state=passwlocker.users[username].login(password=password)
		if state:
			self.userobject=passwlocker.users[username]
			self.successlogin()
		else:
			self.errorlogin()
	def savecred(self):
		self.userobject.add_password()#endelea hapa
	def doadduser(self):
		pass
welcome = WelcomeFrame(root)

root.protocol("WM_DELETE_WINDOW", passwlocker.export)
root.mainloop()
