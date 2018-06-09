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
	def login(self):
		self.password=input(f"Type password for {self.name}:").encode('utf-8')
		if not self.verifyhash():
			print('Wrong password!')
			self.login()
		else:
			self.decrypt()
	def decrypt(self):
		self.decrypted=True
		for encr in self.encrypts:
			try:
				encname,encpass,encsalt=encr.split(':')
				tmp=Credential(userpass=self.password,encrypted=encpass,salt=encsalt)
				self.logins[encname]=tmp
			except:
				pass
	def add_password(self):
		encname=input("Login:")
		uname=input("Username:")
		passw=input("Password:")
		tmp=Credential(username=uname,plaintext=passw,userpass=self.password)
		tmp.encrypt()
		self.logins[encname]=tmp
	def export(self):
		yield self.name+':'+self.loginhash
		if self.decrypted:
			for name,cred in self.logins.items():
				yield '\n\t'+name+':'+cred.export()
		else:
			yield '\n\t'+'\n\t'.join(self.encrypts)
	def updatemaster(self):
		self.password=input("Type current password:").encode('utf-8')
		if self.verifyhash():
			self.password=input("Type new password:").encode('utf-8')
			self.loginhash=sha512(self.password).hexdigest()
			#We also have to reencrypt our passwords
			map(lambda x:x.shiftkey(self.password),self.logins.values())
			print(self.logins)
			print("Password updated successfully")
		else:
			print("Wrong password!")
			raise KeyboardInterrupt
	def show(self):
		for name,cred in self.logins.items():
			print('\n\t'+name+'\t'+cred.decrypt())
	def interactive(self):
		self.login()
		while True:
			try:
				choice=input("""Select an option:
	1.Add Login credential
	2.Show saved credentials
	3.Update Master key
	4.Logout\n""")
				if choice=='1': self.add_password()
				elif choice=='2': self.show()
				elif choice=='3': self.updatemaster() 
				elif choice=='4': return
			except KeyboardInterrupt:
				print("You have been logged out!")
				break