#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class messageInfo:
	"""docstring for messageInfo: manage message user"""
	def __init__(self):
		# for costumers
		self.alpha = None    # add new alphabet
		self.cryptKey = None # add Private Key
		self.cryptExt = None # add extend crypt func
	def cryptReply(self, reply):
		cReply = reply
		return cReply
	# def messageFormat(uid):
