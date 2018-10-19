# -*- coding: utf-8 -*-
import json

def readjson(url):
	self.data={}
	try:
		with open(url) as json_file:
			return json.load(json_file)
	finally:
		return self.data
    



