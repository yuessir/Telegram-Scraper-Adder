#!/bin/env python3
# code by : Termux Professor

"""

you can re run setup.py 
if you have added some wrong value

"""
import os, sys
import configparser
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
def banner():
	os.system('clear')
	print(
		re + " __    __  .______    _______ .______       __        ______   ____    ____  _______     _______.     ______   ______   .___  ___. ")
	print(
		gr + "|  |  |  | |   _  \  |   ____||   _  \     |  |      /  __  \  \   \  /   / |   ____|   /       |    /      | /  __  \  |   \/   | ")
	print(
		re + "|  |  |  | |  |_)  | |  |__   |  |_)  |    |  |     |  |  |  |  \   \/   /  |  |__     |   (----`   |  ,----'|  |  |  | |  \  /  | ")
	print(
		re + "|  |  |  | |   _  <  |   __|  |      /     |  |     |  |  |  |   \      /   |   __|     \   \       |  |     |  |  |  | |  |\/|  | ")
	print(
		re + "|  `--'  | |  |_)  | |  |____ |  |\  \----.|  `----.|  `--'  |    \    /    |  |____.----)   |    __|  `----.|  `--'  | |  |  |  | ")
	print(
		re + " \______/  |______/  |_______|| _| `._____||_______| \______/      \__/     |_______|_______/    (__)\______| \______/  |__|  |__| ")

	print(cy + "version : 1.01")
	print(cy + "Make sure you Subscribed Uber LoverS")
	print(cy + "https://t.me/ubo520")
banner()
print(gr+"[+] Installing requierments ...")
os.system('python3 -m pip install telethon')
os.system('pip3 install telethon')
banner()
os.system("touch config.data")
cpass = configparser.RawConfigParser()
cpass.add_section('cred')
xid = input(gr+"[+] enter api ID : "+re)
cpass.set('cred', 'id', xid)
xhash = input(gr+"[+] enter hash ID : "+re)
cpass.set('cred', 'hash', xhash)
xphone = input(gr+"[+] enter phone number : "+re)
cpass.set('cred', 'phone', xphone)
setup = open('config.data', 'w')
cpass.write(setup)
setup.close()
print(gr+"[+] setup complete !")
print(gr+"[+] now you can run any tool !")
print(gr+"[+] make sure to read docs 4 installation & api setup")
print(gr+"[+] https://github.com/termuxprofessor/TeleGram-Scraper-Adder/blob/master/README.md")
