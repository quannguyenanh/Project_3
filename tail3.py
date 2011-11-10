import time
from sys import argv
import os
import pyinotify

wm = pyinotify.WatchManager()
mask = pyinotify.IN_MODIFY

class PTmp(pyinotify.ProcessEvent):
	def process_IN_MODIFY(self, event):
		pass

def tail_n(filename, line_no):
	list_line = []

	for line in open(filename, 'r'):
		list_line.append(line.strip())
	
	for i in xrange(len(list_line)-line_no, len(list_line)):
		print list_line[i]
		
def tail_f(filename):
	notifier = pyinotify.Notifier(wm, PTmp())
	wdd = wm.add_watch(filename, mask, rec=True)
	file = open(filename, 'r')
	while True:
		try:
			where = file.tell()
			line = file.readline()
		
			if not line and notifier.check_events():
				file.seek(where)
			else:
				print line,
		except KeyboardInterrupt:
			notifier.stop()
			break

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