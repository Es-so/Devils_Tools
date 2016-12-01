#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from mechanize import Browser
import os
import sys
import fbchat
import requests
from lxml import html
from subprocess import call

os.system("clear")

#__________DATA_REQUIEREMENT_____________________________________________________#

USERNAME = raw_input('LOGIN/MAIL: '); 
PASSWORD = raw_input('MDP: ');
LOGIN_URL = "https://www.facebook.com"
TARGET_MP = raw_input('FRIENDS: ');
TARGET = TARGET_MP;
URL_MESS = "https://www.facebook.com/messages/" + TARGET_MP.replace(' ', '.');


# __MULTIPLE_MESSAGES_USER_______________________________


try:
	with open(raw_input("TARGETS USERS FILE: "), "r") as ins:
	    TARGETS = []
	    for line in ins:
	        TARGETS.append(line)
	friend = None

except:
	TARGETS = TARGET
	if TARGETS == None :
		print "No TARGET(S)"
		sys.exit()

#_______________________________________________________

MESSAGE = raw_input('MESSAGE: ')

print ("\n" + "_" * 60 + "\n\033[33m Resume:\033[39m\n" +
	"USERNAME: " + USERNAME + "\n" +
	"URL: " + LOGIN_URL + "\n" +
	"MESSAGE: " + MESSAGE + "\n" +
	"TARGETS: " + str(TARGETS) + "\n" + "_" * 60);

#__________END_DATA_REQUIEREMENT_________________________________________________#

client = fbchat.Client(USERNAME, PASSWORD);

print "\n\n\033[33mSending...\033[39m\n"

if friend is None:
	friends = []
	for selected_target in TARGETS:
		friends.append(client.getUsers(selected_target))
	try:
		for f in friends:
			save_stdout = sys.stdout
			sys.stdout = open('/dev/null', 'w')
			sent = client.send(f[0].uid, "Wesh " + str(f[0].name) + " " + MESSAGE);
			sys.stdout = save_stdout
			if sent:
				print (str(f[0].name) + "\033[32m [√] \033[39m")
			else:
				print (str(f[0].name) + "\033[31m [X] \033[39m")
	except:
		print ("\033[31m Error \033[39m")

else:
	friend = client.getUsers(TARGET)
	save_stdout = sys.stdout
	sys.stdout = open('/dev/null', 'w')
	sent = client.send(friend[0].uid, "Wesh " + str(friend[0].name) + " " + MESSAGE);
	sys.stdout = save_stdout
	if sent:
		print (str(friend[0].name) + "\033[32m [√] \033[39m")
	else:
		print (str(friend[0].name) + "\033[31m [X] \033[39m")


print ("\n\033[32m ... End message(s)\033[39m\n")
