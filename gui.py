from Tkinter import *
from program import Program

root = Tk()
passwlocker=Program()

class WelcomeFrame(Frame):
	def __init__(self, master):
		master.title("Passlocker 1.0")
		Frame.__init__(self, master)
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
	#Interactive methods -->
	def dologin(self):
		try:
			passwlocker.users[self.unameentry.get()].login(password=self.passentry.get())
		except ValueError:
			print("wrong password")
			pass
	def doadduser(self):
		pass
welcome = WelcomeFrame(root)

root.protocol("WM_DELETE_WINDOW", passwlocker.export)
root.mainloop()
