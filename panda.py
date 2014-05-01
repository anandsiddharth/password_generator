#!/usr/bin/python
#This code is completly legal for use for eductional purpose.
#No Evil Activities must be performed.
#Use of the generated password file is allowed with any of the bruteforce utility.
#>x-c0der is watching you<
# +=======================================|
# ||						      		
# ||	x-c0der				      
# ||	do not copy 			      
# ||	private c0de.
# ||	http://x-c0der.yzi.me
# ||	i will irritate the frauders
# ||
# +=======================================|

import sys
import array
import string

plus = '\033[92m'"[ + ] "'\033[0m'
minus = '\033[93m'"[ - ] "'\033[0m'
star = '\033[94m'"[ * ] "'\033[0m'
ques = '\033[95m'"[ ? ] "'\033[0m'
banner = '''
||---> x-c0der's
||---> bruteforcing password file generator
||---> method social engineering :>
||---> its always about hacking :)
||---> mailto:anandsiddharth21@gmail.com
'''
wrn = []
wrn.append(star+"Copying the code and changing the description wont make you a c0der. :)")
wrn.append(star+"The quiter You become, The More You Are Able to Hear")
wrn.append(star+"Answer Most of the questions so that chances of password match would be more.")
wrn.append(star+"Press Ctrl+C anytime to create the password file of whatever you answered")
print banner
for text in wrn:
	print text
#CODE BEGINS HERE
def pass_file():
	global passfilename
	passfilename = str(raw_input(ques+"Enter The Name of Password File you want to create: "))
	global passfile 
	passfile = open(passfilename+".pass","w")
	if not passfile:
		print minus+"Could Not Create File. Please reenter or check folder permissions"
		pass_file()
def victim_name():
	fname = str(raw_input(ques+"Enter the first name of the victim: "))
	lname = str(raw_input(ques+"Enter the last name of the victim: "))
	if  fname == "" and lname == "":
		print minus+"This is required. Please Enter appropriate Value"
		victim_name()
	else:
		passwd.append(fname)
		passwd.append(lname)
def victim_sex():
	sex = raw_input(ques+"Victim's sex [M/F]: ")
	if(sex != 'M' and sex != "m" and sex != "F" and sex != "f"):
		print minus+"Please enter the value as required mentioned inside square brackets"
		victim_sex()
	else:
		return False
#---------------------------------
def exit():
	print plus+"Total Passwords Created: %d" % len(passwd)
	print star+"Writing Passwords to %s.pass !!!" % passfilename
	for password in passwd:
		passfile.write(password+"\n")
	sys.exit(1)
try:
	print "\n"
	passwd = []
	pass_file()
	victim_name()
	victim_sex()
	exit()
except KeyboardInterrupt:
	print "\n"
	print minus+"Keyboard Interrupt"
	exit()
#---------------------------------
