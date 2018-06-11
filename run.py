from program import Program
from prints import *
from getpass import getpass
from time import sleep
passwlocker=Program()
import sys
#This is the in Terminal version of the program use gui.py for graphical version
def showcreds(username):
	userobject=passwlocker.users[username]
	credentials=[pair for pair in userobject.show(show='')]
	# While true pia hapa
	columns=['', 'Username','Password']
	lines=(len(credentials)*3+2)
	print_s(tabulate(credentials,columns,'grid'))
	while True:
		print("Type:")
		print("\tshow name ->show in clear")
		print("\tcopy name ->copy name to clipboard")
		print("\tquit ")
		choice=input("")
		clearterm(lines+3)
		if choice.startswith("show"):
			name=choice.split(" ")[1]
			credentials=[pair for pair in userobject.show(show=name)]
			lines=(len(credentials)*3+2)
			print_s(tabulate(credentials,columns,'grid'))
		elif choice.startswith("copy"):
			name=choice.split(" ")[1]
			text=userobject.logins[name].copy()
			print_s(f"{name} has been copied to clipboard")
			lines=0
			sleep(1)
			clearterm(0)
		elif choice=='quit':
			break
		pass
def addcred(username):
	userobject=passwlocker.users[username]
	name=input("Name:")
	if name in userobject.logins.keys():
		print_e(f"Entry {name} already exists")
		sleep(1)
		clearterm(1)
		return
	user=input("Username:")
	passw=input("Password:")
	success=userobject.add_password(name,user,passw)
	if success:
		clearterm(2)
		print_s(f"Entry {name} added successfully")
		sleep(1)
		clearterm(0)
def changemaster(username):
	old=input("Old Password:")
	new=getpass("New Password:")
	clearterm(1)
	userobject=passwlocker.users[username]
	success=userobject.updatemaster(old,new)
	if success:
		print_s("Password updated successfully")
	else:
		print_e("Wrong initial password!")
	sleep(1)
	clearterm(0)
	raise KeyboardInterrupt
def manage(username,password):
	try:
		while True:
			print("Choose an Option:")
			print("\t1.Show Stored credentials")
			print("\t2.Add a credential")
			print("\t3.Change Master password")
			print("\t4.Back")
			choice=input("")
			clearterm(6)
			if choice=='1':
				showcreds(username)
			elif choice=='2':
				addcred(username)
			elif choice=='3':
				changemaster(username)
			elif choice=='4':
				break
	except KeyboardInterrupt:
		pass
def login():
	username=input("Type your username:")
	if username not in passwlocker.users.keys():
		print_e("Username not Recognized")
		sleep(1)
		clearterm(1)
		return
	password=getpass("Type your password:")
	clearterm(1)
	success=passwlocker.users[username].login(password=password)
	if success:
		print_s("Login successfull")
		sleep(1)
		manage(username,password)
	else:
		print_e("Wrong password!")
		sleep(1)
		clearterm(0)
def create():
	name=input("Username:")
	if name in passwlocker.users.keys():
		print_e("Username already exists")
		sleep(1)
		clearterm(1)
		return
	passw=getpass("Password:")
	success=passwlocker.adduser(name,passw)
	clearterm(1)
	if success:
		print_s(f"User {name} added successfully")
		sleep(1)
		clearterm(0)
try:
	banner()
	while True:
		print("Select an Option:")
		print("\t1.Login")
		print("\t2.Create an Account")
		print("\t3.Quit")
		choice=input("")
		clearterm(4)
		if choice=='1':
			login()
		elif choice=='2':
			create()
		elif choice=='3':
			passwlocker.export()
except KeyboardInterrupt:
	passwlocker.export()