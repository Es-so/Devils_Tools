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
from bs4 import BeautifulSoup
import json
from pprint import pprint
import messClass
from messClass import messageInfo

os.system("clear")
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

#__________DATA_REQUIEREMENT_____________________________________________________#

USERNAME = raw_input('LOGIN/MAIL: '); 
PASSWORD = raw_input('MDP: ');
LOGIN_URL = "https://www.facebook.com/login.php"
MESSAGE_URL = "https://www.facebook.com/messages"
# client = fbchat.Client(USERNAME, PASSWORD);

#__________END___________________________________________________________________#


def callBrowser(url):
	br = Browser()
	br.set_handle_robots( False )
	br.addheaders = [('User-agent', 'Firefox')]
	br.open(url)
	return br


def startConnect(browser):
	browser.select_form(nr=0)
	browser['email'] = USERNAME
	browser['pass'] = PASSWORD
	browser.submit()
	return browser


def getPage(url):
	brPage = callBrowser(url)
	r = startConnect(brPage)
	rc = startConnect(brPage)
	return brPage


def span_nbMess(page_html):
	nb_newMess = BeautifulSoup(page_html, "lxml")
	for span in nb_newMess.find_all('span'):
		if span.get('id') == "mercurymessagesCountValue":
			return span


def getListOfAuthors(data):
	client = fbchat.Client(USERNAME, PASSWORD)
	listMess = {}
	# for Id in ids:
	# 	print str(Id[0]) + ' | ' + str(ids[0][0])
	# 	friend_info = client.getUserInfo(str(Id[0]))
	# 	print friend_info['name']
	# 	# listMess[friend_info['name']] = ": unread = " + Id[1]
	# print "__"*45 + "\n"
	# print str(listMess)
	print "__"*45 + "\n"
	# print friend1_info['name']


def getAuthorsOfMess(url):
	messPage = callBrowser(url)
	for form in messPage.forms():
		print str(form)
	messPage = startConnect(messPage)
	response = startConnect(messPage).response()
	print "__"*45 + "\n"*20
	jsRep = re.findall(r"{thread.*thread_fbid:.*unread_count:[0-9]*.*work_user_warning_dismiss_count:{}}",response.read())
	jsRepTh = re.findall(r'{(thread_id:\"(.).*?thread_fbid:\"([0-9]+)\".*?participants:\[(.*?)\].*?unread_count:([1-9]+).*?\{\})\}',jsRep[0], re.MULTILINE)
	if (jsRepTh != None):
		dataMess = messageInfo().userList(jsRepTh)
		for key, value  in dataMess.iteritems():
			print key + " => " + str(value)
		if (dataMess != None):
			getListOfAuthors(dataMess)

def readMess(target):
	# friend = client.getUsers(target)
	# friend_info = client.getUserInfo(friend[0].uid)
	# last_messages = client.getThreadInfo(friend[0].uid,0)
	# last_messages.reverse()  # messages come in reversed order
	# print (last_messages)

def messagerie():
	br = getPage(LOGIN_URL)
	print  br.response().read()
	print "__"*45 +"\n"*20
	find = span_nbMess(br.response())
	nbMess = re.findall(r".*>(.*)<.*", str(find));
	print nbMess[0]
	print "__"*45 + "\n"*20
	if int(nbMess[0]) != 0:
		getAuthorsOfMess(MESSAGE_URL)