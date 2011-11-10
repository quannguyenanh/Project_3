import time
from sys import argv

def tail_n(filename, line_no):
	list_line = []

	for line in open(filename, 'r'):
		list_line.append(line.strip())
	
	for i in xrange(len(list_line)-line_no, len(list_line)):
		print list_line[i]
		
def tail_f(filename):
	file = open(filename, 'r')
	interval = 1
	while 1:
		where = file.tell()
		line = file.readline()
		if not line:
			time.sleep(interval)
			file.seek(where)
		else:
			print line,

if len(argv) == 2:	
	filename = argv[1]
	line_no = 10
	tail_n(filename, line_no)
elif argv[1] == '-n':
	line_no = int(argv[2])
	filename = argv[3]
	tail_n(filename, line_no)
elif argv[1] == '-f':
	filename = argv[2]
	tail_f(filename)
