#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class messageInfo:
	"""docstring for messageInfo: manage message user"""
	
	def __init__(self):
		self.name_regex = '[^Aa-zZ]name:\"(.*?)\"'
		self.regexTable = r'[^Aa-zZ_]thread_id:\"(.).*?thread_fbid:\"([0-9]+)\".*?participants:\[(.*?)\].*?name:\"(.*?)\".*?unread_count:([0-9]+).*?'
	
	def userList(self, data):
		if data:
			dataMess = {}
			for da in data:
				user = []
				thread =  da[1]
				name = da[3]
				letter = da[0]
				uid = da[1]
				participants = re.findall(r'fbid:([0-9]+)\"', da[2])
				unread = da[4]
				user.extend([letter, name, participants, unread])
				dataMess[uid] = user
			return dataMess
		return None
