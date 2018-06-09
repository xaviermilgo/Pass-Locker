from hashlib import sha512,pbkdf2_hmac
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode,urlsafe_b64decode
from os import urandom
class Credential:
	def __init__(self,plaintext='',username='',userpass='',encrypted='',salt=''):
		self.__password=plaintext
		self.key=userpass
		self.username=username
		self.encrypted=bytes(encrypted,'utf-8')
		self.salt=urandom(16) if salt=='' else urlsafe_b64decode(salt)
		ekey=pbkdf2_hmac('sha256',self.key,self.salt, 100000)
		self.enckey=urlsafe_b64encode(ekey)
	def encrypt(self):
		fernet=Fernet(self.enckey)
		self.encrypted=fernet.encrypt(bytes(self.username+':::'+self.__password,'utf-8'))
	def decrypt(self):
		fnet=Fernet(self.enckey)
		uname,upass=fnet.decrypt(self.encrypted).split(b':::')
		return b':'.join([uname,upass]).decode('utf-8')
	def export(self):
		return self.encrypted.decode('utf-8')+':'+urlsafe_b64encode(self.salt).decode('utf-8')

class User:
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
			self.show()
			self.add_password()
			self.show()
	def decrypt(self):
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
		for name,cred in self.logins.items():
			yield '\n\t'+name+':'+cred.export()
	def show(self):
		print(f'{self.name}:{self.password}')
		for name,cred in self.logins.items():
			print('\n\t'+name+':'+cred.decrypt())
		print(self.logins)


class Program:
	users={}
	def __init__(self,configfile='progdata'):
		self.parse(configfile)
		print(self.users)
		self.users['Xavier'].login()
		self.export(configfile)
	def parse(self,configfile):
		with open(configfile) as conf:
			data=conf.read().split('\n\n')
		for user in data:
			userdata={}
			username=user.split('\n\t')[0].split(':')[0]
			userdata['passhash']=user.split('\n\t')[0].split(':')[1]
			userdata['encrypts']=user.split('\n\t')[1:]
			self.users[username]=User(username,userdata)
	def export(self,configfile):
		with open(configfile,'w') as wr: 
			for name,userobject in self.users.items():
				wr.write(''.join(userobject.export()))
passwlocker=Program()