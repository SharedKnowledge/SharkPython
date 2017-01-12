# -*- coding: utf-8 -*-
from SemanticTag import *
from Exceptions import TypeError
class Payload(object):
	values = None
	topic = None
	def __init__(self, sender, topic):
		self.values = []
		if (isinstance(topic, Topic)):
			self.topic = topic
		else:
			raise TypeError("topic", "Topic")

		if (isinstance(sender,Sender)):
			self.sender = sender
		else:
			print type(Sender)
			raise TypeError("sender", "Sender")

	''' Vergleicht 2 Payloads,
			same = True, wenn die Topics gleich sind
			newer = True, wenn Topic gleich & die values von other sind im Payload enthalten
	'''
	def same_as(self, other):
		same = False
		newer = False
		if (self.topic.si == other.topic.si):
			if (self.values == other.values):
				same = True
			if len(self.values)>len(other.values) and len(set(other.values).intersection(self.values)) == len(other.values):
				same = True
				newer = True
		return (same, newer)

	#add value to list
	def add_value(self, value):
		self.values.append(value);

	#replace value(s)
	def new_value(self, value):
		self.values = value
	#return last values
	def last(self):
		return self.values[-1]

	def __str__(self, long=False):
		if long:
			return "[%s]: %s" % (self.topic, self.values)
		else:
			return "[%s]: %s" % (self.topic.name,self.values)

class Measurement(Payload):
	def __init__(self, sender, topic, unit):
		Payload.__init__(self, sender, topic)
		# Remove Spaces and convert to Uppercase
		self.unit = unit.replace(' ','').upper()

	def __str__(self, long=False):
		if long:
			return "[%s][%s]: %s" % (self.topic, self.unit, self.values)
		else:
			return "[%s][%s]: %s" % (self.topic, self.unit, self.values)
