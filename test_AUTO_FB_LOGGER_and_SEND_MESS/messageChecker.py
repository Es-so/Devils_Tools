#!/usr/bin/env python
#-*- coding: utf-8 -*-

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
client = fbchat.Client(USERNAME, PASSWORD);

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
	listUnread = []
	i = 0
	for key, value in data.iteritems():
		if len(value[2]) > 2:
			name = value[1]
		else:
			name = client.getUserInfo(str(key))['name']
		listUnread.append(dict({'title' : name,\
								'type' : value[0],\
								'ID' : key,\
								'nbUnread' : value[3]}))

	# print "FINALE:\n" + str(listUnread)
	return listUnread


def getThreadsOfMess(url):
	messPage = callBrowser(url)
	messPage = startConnect(messPage)
	response = startConnect(messPage).response()
	jsRepTh = re.findall(r"[^Aa-zZ_]thread_id:\"(.).*?thread_fbid:\"([0-9]+)\".*?participants:\[(.*?)\].*?name:\"(.*?)\".*?unread_count:([0-9]+).*?",response.read())
	if (jsRepTh != None):
		dataMess = messageInfo().userList(jsRepTh)
	if (dataMess != None):
		return getListOfAuthors(dataMess)

def readMess(target):
	# friend = client.getUsers(target)
	# friend_info = client.getUserInfo(friend[0].uid)
	last_messages = client.getThreadInfo(target,0)
	last_messages.reverse()  # messages come in reversed order
	# content = client._parseMessage(last_messages)
	# if 'ms' not in content: return
	# 	for m in content['ms']:
	# 		print str(content['ms'])

	ret = []
	for message in last_messages:
		# ret.append(message['message']['sender_name'])
		ret.append(message.body)
	return (ret)

def messagerie():
	br = getPage(LOGIN_URL)
	#print  br.response().read()
	find = span_nbMess(br.response())
	nbMess = re.findall(r".*>(.*)<.*", str(find));
	#print nbMess[0]
	if int(nbMess[0]) != 0:
		return getThreadsOfMess(MESSAGE_URL)
	return None

def getUnread():
	return messagerie()

getUnread()