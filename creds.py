from hashlib import pbkdf2_hmac
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode,urlsafe_b64decode
from os import urandom
import pyperclip

class Credential:
	'''
	Class that holds info about a credential
	'''
	def __init__(self,plaintext='',username='',userpass='',encrypted='',salt=''):
		'''
		Initializes both a new and existing credential object
		'''
		self.__password=plaintext
		self.key=userpass
		self.username=username
		self.encrypted=bytes(encrypted,'utf-8')
		self.salt=urandom(16) if salt=='' else urlsafe_b64decode(salt)
		ekey=pbkdf2_hmac('sha256',self.key,self.salt, 100000)
		self.enckey=urlsafe_b64encode(ekey)
	def encrypt(self):
		'''
		Encrypts a credential object for storage using the mater key
		'''
		fernet=Fernet(self.enckey)
		self.encrypted=fernet.encrypt(bytes(self.username+':::'+self.__password,'utf-8'))
	def decrypt(self,hide=False):
		'''
		Decrypts a credential object in order to display it to the user
		'''
		fnet=Fernet(self.enckey)
		uname,passw=fnet.decrypt(self.encrypted).decode('utf-8').split(':::')
		if hide:
			passw='*'*len(passw)
		return [uname,passw]
	def shiftkey(self,newpass):
		'''
		Rencrypts a credential after the user changes the master key
		'''
		old=Fernet(self.enckey)
		ekey=pbkdf2_hmac('sha256',newpass,self.salt, 100000)
		self.enckey=urlsafe_b64encode(ekey)
		new=Fernet(self.enckey)
		self.encrypted=new.encrypt(old.decrypt(self.encrypted))
	def copy(self):
		'''
		copies the decrypted password to clipboard
		'''
		pyperclip.copy(self.decrypt()[1])
	def export(self):
		'''
		Prepares the credential object for exportation
		'''
		return self.encrypted.decode('utf-8')+':'+urlsafe_b64encode(self.salt).decode('utf-8')