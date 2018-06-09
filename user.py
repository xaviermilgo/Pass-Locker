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
			encname,encpass,encsalt=encr.split(':')
			tmp=Credential(userpass=self.password,encrypted=encpass,salt=encsalt)
			self.logins[encname]=tmp
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
	def show(self):
		print(f'{self.name}:{self.password}')
		for name,cred in self.logins.items():
			print('\n\t'+name+':'+cred.decrypt())
		print(self.logins)
	def interactive(self):
		pass