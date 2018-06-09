class Program:
	users={}
	def __init__(self,configfile='progdata',use_gui=False):
		self.configfile=configfile
		self.use_gui=use_gui
		self.parse()
	def begin(self):
		try:
			self.interactive()
		except KeyboardInterrupt:
			pass
		print("Saving configuration ...")
		self.export()
	def tkintergui(self):
		import tkinter
	def interactive(self):
		pass
	def adduser(self,name,password):
		password=sha512(password).hexdigest()
		userdata={
			'passhash':password,
			'encrypts':[]
		}
		if name in self.users.keys():
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