from user import User
from hashlib import sha512

class Program:
	'''
	Class that contains entire program details and methods
	'''
	users={}
	def __init__(self,configfile='progdata'):
		'''
		Initializes the program with a config file
		'''
		self.configfile=configfile
		self.parse()
	def adduser(self,name,password):
		'''
		Adds a user object to the program
		'''
		password=sha512(password.encode('utf-8')).hexdigest()
		userdata={
			'passhash':password,
			'encrypts':[]
		}
		if name in self.users.keys():
			print("A user already exists with that username!")
			return False
		self.users[name]=User(name,userdata)
		return True
	def parse(self):
		'''
		Parses the config file to recover stored user objects
		'''
		with open(self.configfile) as conf:
			data=conf.read().split('\n\n')
		for user in data:
			if user=='': continue
			userdata={}
			username=user.split('\n\t')[0].split(':')[0]
			userdata['passhash']=user.split('\n\t')[0].split(':')[1]
			userdata['encrypts']=user.split('\n\t')[1:]
			self.users[username]=User(username,userdata)
	def export(self):
		'''
		Exports the userobjects and writes them to the config file
		'''
		with open(self.configfile,'w') as wr: 
			usersdata=[''.join(obj.export()) for obj in self.users.values()]
			wr.write('\n\n'.join(usersdata))
		exit(0)