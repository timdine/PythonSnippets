#!/usr/bin/env python

"""parseSDEIntercept.py: Parse an SDE Intercept Log file to quickly find issues."""


__author__      = "Tim Dine"
__maintainer__ = "Tim Dine"
__email__ = "timdine@hotmail.com"
__status__ = "Development"


import re
import datetime

now = datetime.datetime.now()
infilepath = r"C:\temp\SDEINTERCEPTLOG\sdeinterceptlog.005"
lasttime = None
currenttime = None
lastCommand = ""
infile = open(infilepath, "r")
for line in infile:
	if "Command:" in line:
		commandTime = line[3:14]
		if lasttime == None:
			lasttime = now.replace(hour=int(commandTime[0:1]), minute=int(commandTime[3:4]), second=int(commandTime[6:7]), microsecond=int(commandTime[9:11]))
			currenttime = lasttime
			lastCommand = line[31:]
			#print lasttime, currenttime
		else:
			currenttime = now.replace(hour=int(commandTime[0:1]), minute=int(commandTime[3:4]), second=int(commandTime[6:7]), microsecond=int(commandTime[9:11]))
			#print lasttime, currenttime
			theCommand = line[31:]
			if (currenttime - lasttime).seconds > 0 and (currenttime - lasttime).seconds < 9999:
				print (currenttime - lasttime).seconds, lastCommand, theCommand, line
			lasttime = currenttime
			lastCommand = theCommand
		#print line, commandTime
		
		
