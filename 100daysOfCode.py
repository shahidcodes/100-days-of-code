def main():
	print("1-%s\n2-%s\n3-%s" % ("Add Log", "Add Timeline", "Exit"))
	logFileName = "log.md"
	timelineFileName = "timeline.md"
	option = int(input(">>> "))
	if option == 1:
		autoMode = str(input("Auto Detect Last Day?(Y/N)\n>>> ")).lower()
		if autoMode == 'y':
			print("""
		[*] Auto mode is only work if you cloned my repo!
		[*] If not then just make your log.md looks like mine.
					(@github.com/shahidkh4n)
				""")
			logFile = open(logFileName, "r")
			lastDayString = logFile.readlines()[-5:-4][0]
			print(lastDayString)
			logFile.close()
			import re
			lastDay = int(re.findall(r'Day [0-9]{2}', lastDayString)[0].split(" ")[1])
			currentDay = lastDay+1
			day = currentDay
			print("[+] Last Day was %s " % (lastDay))
		else:
			day = str(input("[-] Current Day (ex. 5)\n>>> "))	
		template = """
### Day {day}: {date}

**Today's Progress**: {progress}

**Thoughts:** {thoughts}"""
		progress = str(input("[-] Progress (I did something 'X')\n>>> "))
		thoughts = str(input("[-] Thoughts (What you feel about it?)\n>>> "))
		import time
		date = time.strftime("%B, %d %Y")
		with open(logFileName, "a") as log:
			log.write(template.format(day=day, date=date, progress=progress, thoughts=thoughts))
		print("[+] Successful")
	elif option == 2:
		autoMode = str(input("Auto Detect Last Timeline?(Y/N)\n>>> ")).lower()
		if autoMode == 'y':
			lastTimeLineNumber = ""
			with open(timelineFileName, "r") as timelineFile:
				lastTimeLineNumber = int( timelineFile.readlines()[-1].strip().split('.')[0] )
			currentTimeLineNumber = lastTimeLineNumber+1
		else:
			currentTimeLineNumber = str(input("[-] Current Time Line Number?\n>>> "))
		
		template = """
	 {timelineNumber}. {timelineDescription}"""
		timelineDescription = str(input("[-] Whats this task is all about?\n>>> "))
		with open(timelineFileName, "a") as timelineFile:
			timelineFile.write(template.format(timelineNumber=currentTimeLineNumber, timelineDescription=timelineDescription))
		print("[+] Successful")
	elif option == 3:
		print("<> Any feedback ? Send here @twitter/sh4hidkh4n")
		exit(0)

if __name__ == "__main__":
	doc = """#################
 This is under development. But its pretty usable.
 I used this on my previous days. So if you find
 any bug just tweet me @sh4hidkh4n with traceback 
 log. Thank you!
#################"""
	print(doc)
	while True:
		main()