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