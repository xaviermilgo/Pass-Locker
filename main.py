from hashlib import sha512,pbkdf2_hmac
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode,urlsafe_b64decode
from os import urandom
from creds import Credential
from program import Program
from user import User

passwlocker=Program(use_gui=False)#Change to true to use Tkinter gui