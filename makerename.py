
import os

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(".") if (isfile(join(".", f)) and f!="rename.py" and f!="makerename.py" and f!="rename.txt")]

longest = 0
for i in onlyfiles:
	if len(i)>longest:
		longest = len(i)

inst =  open("rename.txt","w")
first = True
for i in onlyfiles:
	if first:
		first = False
	else:
		inst.write("\n")	
	inst.write(i.ljust(longest,' ') + ":" + i);
inst.close()