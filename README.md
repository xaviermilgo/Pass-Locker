#   _________________
#  :                 :
# |   PASS LOCKER 1   |
#  :_________________:

### Author: Xavier Kibet

## Description
[Pass Locker](https://github.com/reivhax/Pass-Locker) allows you to securely
store your online or offline credentials using a master key.

![Run.py](http://i.imgur.com/FbBNwHr.png)
## OR
![Gui.py](http://i.imgur.com/qwtNjc6.png)

## Specs

1. Add Users
2. Login as a specific user
3. Add credentials
4. Randomly generate credentials
5. List stored credentials
6. Copy passwords to clipboard

## Setup
#### First clone this repo:
```
git clone https://github.com/reivhax/Pass-Locker.git
cd Pass-Locker
```
#### Install requirements
```pip install -r requirements.txt```

#### You can now run the code
```
python run.py
```
##### or 
```
python gui.py
```
## How it works
The program is made of Four main modules that are 'stacked' on top of each other.

![Stack](http://i.imgur.com/0Dq9qXS.png)

As shown in the image:
. At the top of the stack is either the in terminal interactive python file or the graphical user interface. It links the user of the program and the program object.
. The Program consists of user objects it is responsible for actions at the user level like creating new users and exporting users.
. The next level is the user level which consits of credential objects. This object is reaposible for creating and exporting credential objects, as well as encrypting itself.
. At the base of this stack is the credential object which stores a particular credential and encrypts itself.

## Security

The user logs in to the system using apassword. This password is hashed using sha512 stored in the progdata file.

The credentials of users are stored within the progdata file but they are encrypted using fernet encryption. The key used in this encryptin is the users master key.

#### Note: This is an academic project. Although it implements security measures such as encryprtion it should not be used as a reliable project. It may have simple bugs that may lead to bigger problems. If you think you have found any bug please inform me.

## License (MIT License)

This project is licensed under the MIT Open Source license, (c) Xavier Kibet 2017.
please refer to [Licence.md](License.md) for more info