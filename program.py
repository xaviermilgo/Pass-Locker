from user import User
from hashlib import sha512

class Program:
	users={}
	def __init__(self,configfile='progdata',use_gui=False):
		self.configfile=configfile
		self.use_gui=use_gui
		self.parse()
	def begin(self):
		try:
			self.tkintergui() if self.use_gui else self.interactive()
		except KeyboardInterrupt:
			pass
		print("Saving configuration ...")
		self.export()
	def tkintergui(self):
		pass
	def interactive(self):
		while True:
			try:
				choice=input("""Select an option:
	1.Login
	2.Create new User
	3.Exit\n""")
				if choice=='1': self.users[input("Name:")].interactive()
				elif choice=='2': self.adduser(input("username:"),input("password:"))
				else: raise KeyboardInterrupt
			except KeyboardInterrupt:
				break
	def adduser(self,name,password):
		password=sha512(password.encode('utf-8')).hexdigest()
		userdata={
			'passhash':password,
			'encrypts':[]
		}
		if name in self.users.keys():
			print("A user already exists with that username!")
			return False
		self.users[name]=User(name,userdata)
	def parse(self):
		with open(self.configfile) as conf:
			data=conf.read().split('\n\n')
		for user in data:
			userdata={}
			username=user.split('\n\t')[0].split(':')[0]
			userdata['passhash']=user.split('\n\t')[0].split(':')[1]
			userdata['encrypts']=user.split('\n\t')[1:]
			self.users[username]=User(username,userdata)
	def export(self):
		with open(self.configfile,'w') as wr: 
			usersdata=[''.join(obj.export()) for obj in self.users.values()]
			wr.write('\n\n'.join(usersdata))