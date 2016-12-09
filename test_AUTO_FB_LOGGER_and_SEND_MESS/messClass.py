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
			# print "0"*60 + str(data) + "0" *60
			# tableData = re.findall(self.regexTable, str(data))
			# for table in data:
			# 	print "---> " + str(table)
			# print ( "||||"*45 + "\n" +
			# str(data) + "\n" +
			# "||||"*45)
			dataMess = {}
			for da in data:
				# print "[[[" * 20 + str(da[1]) + "]]]" * 20
				user = []
				thread =  da[1]
				name = da[3]
				letter = da[0]
				uid = da[1]
				participants = re.findall(r'fbid:([0-9]+)\"', da[2])
				# print "SISICHAKAL: " +  str(len(participants))
				unread = da[4]
				user.extend([letter, name, participants, unread])
				# print user
				dataMess[uid] = user
				# print "\n" * 20 + "v"
				# print dataMess
			# print ">>>" * 50 + str(dataMess) + "<<<" * 50
			return dataMess
		return None
	# def messageFormat(uid):
