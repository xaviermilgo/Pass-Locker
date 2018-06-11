import sys
from tabulate import tabulate
class printer():
	"""
	This class is just a custom implementation of the print function with color functionality.
	"""
	colors = {
		'OKGREEN' :'\033[92m',
		'WARNING' : '\033[93m',
		'FAIL' : '\033[91m',
		'ENDC': '\033[0m' }
	def __init__(self,CLR):
		self.color = self.colors[CLR]
		self.term = self.colors['ENDC']

	def __call__(self,text):
		print(self.color +text+self.term)

print_s = printer('OKGREEN')
print_w = printer('WARNING')
print_e = printer('FAIL')

def clearterm(lines):
	sys.stdout.write("\033[K\033[F"*(lines+1)+"\033[K")
def banner():
	print_w(r"""
     .--------.
    / .------. \
   / /        \ \
   | |        | |
  _| |________| |_
.' |_|        |_| '.
|   PASS  LOCKER   |
'._____ ____ _____.'
|     .'____'.     |
'.__.'.'    '.'.__.'
'.__  | v1.0 |  __.'
|   '.'.____.'.'   |
'.____'.____.'____.'
'.________________.'""")