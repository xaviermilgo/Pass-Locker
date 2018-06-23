from hashlib import sha512
from creds import Credential

class User:
	'''
	Class that hold infomation about a user
	'''
	decrypted=False
	def __init__(self,username,userdata):
		'''
		Initializes an existing user or creates a new one
		'''
		self.name=username
		self.loginhash=userdata['passhash']
		self.encrypts=userdata['encrypts']
		self.logins={}
	def verifyhash(self):
		'''
		verifies hash on user login
		'''
		hash=sha512((self.password).encode('utf-8'))
		return hash.hexdigest()==self.loginhash
	def login(self,password=''):
		'''
		starts login and tries to decrypt user creds
		'''
		self.password=password
		if not self.verifyhash():
			return False
		else:
			self.decrypt()
			return True
		if encname in self.logins.keys():
			return False
		tmp=Credential(username=uname,plaintext=passw,userpass=bytes(self.password,'utf-8'))
	def decrypt(self):
		'''
		Decryots all child credentials of this user
		'''
		self.decrypted=True
		for encr in self.encrypts:
			if encr=='': continue
			encname,encpass,encsalt=encr.split(':')
			tmp=Credential(userpass=bytes(self.password,'utf-8'),encrypted=encpass,salt=encsalt)
			self.logins[encname]=tmp
	def add_password(self,encname,uname,passw):
		'''
		Adds a credential to the user space
		'''
		if encname in self.logins.keys():
			return False
		tmp=Credential(username=uname,plaintext=passw,userpass=bytes(self.password,'utf-8'))
		tmp.encrypt()
		self.logins[encname]=tmp
		return True
	def export(self):
		'''
		Exports user object for storage including all child credentials
		'''
		yield self.name+':'+self.loginhash
		if self.decrypted:
			for name,cred in self.logins.items():
				yield '\n\t'+name+':'+cred.export()
		else:
			yield '\n\t'+'\n\t'.join(self.encrypts)
	def updatemaster(self,current,newpass):
		'''
		Changes the master password used by the user
		'''
		self.password=current
		if self.verifyhash():
			self.password=newpass.encode('utf-8')
			self.loginhash=sha512(self.password).hexdigest()
			for cred in self.logins.values():
				cred.shiftkey(self.password)
			return True
		else:
			return False
	def show(self,show=False):
		'''
		Returns a list of decrypted credentials by belonging to this user
		'''
		if show!=False:
			for name,cred in self.logins.items():
				creds=cred.decrypt(hide=show!=name)
				yield [name]+creds
		else:
			for name,cred in self.logins.items():
				creds=cred.decrypt()
				yield [name]+creds