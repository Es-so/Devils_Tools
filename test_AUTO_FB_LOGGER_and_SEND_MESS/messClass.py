#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class messageInfo:
	"""docstring for messageInfo: manage message user"""
	def __init__(self):
		self.name_regex = '[^Aa-zZ]name:\"(.*?)\"'
	def userList(self, data):
		if data:
			dataMess = {}
			for da in data:
				user = []
				thread =  da[0]
				name = str(re.findall(self.name_regex, da[0]))
				letter = da[1]
				uid = da[2]
				participants = da[3]
				unread = da[4]
				user.extend([letter, name, participants, unread])
				dataMess[uid] = user
		return dataMess
