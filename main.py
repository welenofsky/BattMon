#! /usr/bin/python3
import subprocess
import time
import os
import sys

battfull = 1

while battfull == 1:
	process = subprocess.Popen("acpi", stdout=subprocess.PIPE);
	#output = process.communicate()[0];
	
	acpi = str(process.stdout.read(), "utf-8") 
	if acpi.find("100%") > 0:
		os.system("aplay test.wav")
		subprocess.Popen(["zenity", "--warning","--text=\'Battery Full!\'"]);
		battfull = 0
	else:
		time.sleep(20);
	time.sleep(5);
	try:
		process.kill()
	except OSError:
		pass

