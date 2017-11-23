
import os


inst =  open("rename.txt","r")
for l in inst:
	try:
		l = l.rstrip()
		l = l.lstrip()
		currentname = l.split(":")[0].lstrip().rstrip()
		newname = l.split(":")[1].lstrip().rstrip()
		os.rename(currentname,newname);
	except:
		print("Failed to Rename: \n" + currentname+ " to\n"+newname)
		
print("Success")
inst.close()
os.system("pause")
