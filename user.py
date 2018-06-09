from hashlib import sha512
from creds import Credential

class User:
	decrypted=False
	def __init__(self,username,userdata):
		self.name=username
		self.loginhash=userdata['passhash']
		self.encrypts=userdata['encrypts']
		self.logins={}
	def verifyhash(self):
		return sha512(self.password).hexdigest()==self.loginhash
	def login(self,password=False):
		self.password=password
		if not self.verifyhash():
			print('Wrong password!')
			return False
		else:
			self.decrypt()
			return True
	def decrypt(self):
		self.decrypted=True
		for encr in self.encrypts:
			# noinspection PyBroadException
			try:
				encname,encpass,encsalt=encr.split(':')
				tmp=Credential(userpass=self.password,encrypted=encpass,salt=encsalt)
				self.logins[encname]=tmp
			except:
				pass
	def add_password(self,encname,uname,passw):
		if encname in self.logins.keys():
			print("Choose another Name")
			return False
		tmp=Credential(username=uname,plaintext=passw,userpass=self.password)
		tmp.encrypt()
		self.logins[encname]=tmp
		return True
	def export(self):
		yield self.name+':'+self.loginhash
		if self.decrypted:
			for name,cred in self.logins.items():
				yield '\n\t'+name+':'+cred.export()
		else:
			yield '\n\t'+'\n\t'.join(self.encrypts)
	def updatemaster(self,current,newpass):
		self.password=current.encode('utf-8')
		if self.verifyhash():
			self.password=newpass.encode('utf-8')
			self.loginhash=sha512(self.password).hexdigest()
			map(lambda x:x.shiftkey(self.password),self.logins.values())
			print("Password updated successfully")
			return True
		else:
			print("Wrong password!")
			return False
	def show(self):
		for name,cred in self.logins.items():
			return [name]+cred.decrypt()
	def interactive(self):
		#Refactor planned