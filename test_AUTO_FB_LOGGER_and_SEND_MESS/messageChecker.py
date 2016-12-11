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

print __file__
USERNAME = raw_input('LOGIN/MAIL: '); 
PASSWORD = raw_input('MDP: ');
LOGIN_URL = "https://www.facebook.com/login.php"
MESSAGE_URL = "https://www.facebook.com/messages"
client = fbchat.Client(USERNAME, PASSWORD);

MENU = 'menu'
EXT = 'extend'
COMMAND = "command"
OPTION_ = []
OPTIONS = [
		{ 'title' : 'Mark as read', 'type' : COMMAND, EXT : '', 'command' : 'MarkAsRead'},
		{ 'title' : 'Reply', 'type' : COMMAND, EXT : '', 'command' : 'Reply'},
		{ 'title' : 'Decrypt', 'type' : COMMAND, EXT : '', 'command' : 'Decrypt', 'body' : 'body', 'timestamp ': 'timestamp'},
		{ 'title' : 'Reply with encription', 'type' : COMMAND, EXT : '', 'command' : 'cryptReply'},
]
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

def getUserName(uid):
	_info = client.getUserInfo(uid)
	name = _info['name']
	return name

def getListOfAuthors(data):
	listUnread = []
	i = 0
	for key, value in data.iteritems():
		if len(value[2]) > 2:
			name = value[1]
		else:
			try:
				name = client.getUserInfo(str(key))['name']
			except:
				name = 'Group'
		listUnread.append(dict({'title'       : name,\
								'type'        : MENU,\
								 EXT          : 'messages',\
								'ID'          : key,\
								'nbUnread'    : value[3],\
								'subtitle'    : 'Select a message',\
								'options'     : OPTION_}))
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

def organizeMess(target):
	last_messages = client.getThreadInfo(target,0)
	last_messages.reverse()  # messages come in reversed order
	ret = []
	i = 0
	message_f = {}
	for message in last_messages:
		text = message.body
		text = text.encode('ascii', 'ignore').decode('ascii')
		uid = re.findall(r'fbid:([0-9]+)', message.author)
		start = text[0:12] + '...'
		_format = str(getUserName(uid[0])) + ": " + start
		ret.append( dict( { 'title'     : _format,\
							'type'      : MENU,\
							 EXT        : 'body',
							'timestamp' : message.timestamp,\
							'body'      : text,\
							'subtitle'  : 'Select an action',\
							'options'   : OPTIONS }))
	return (ret)

def readMess(target):
	# friend = client.getUsers(target)
	# friend_info = client.getUserInfo(friend[0].uid)
	last_messages = client.getThreadInfo(target,0)
	last_messages.reverse()  # messages come in reversed order
	ret = []
	i = 0
	for message in last_messages:
		text = message.body
		uid = re.findall(r'fbid:([0-9]+)', message.author)
		# return str(uid[0])
		_format = str(getUserName(uid[0])) + ": " + text
		# ret.append(message['message']['sender_name'])
		ret.append(_format)
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

# getUnread()
