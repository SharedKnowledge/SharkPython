"""This class and its derivations are the Python implementations of the ASIP structures
The classes are implemented according to the the asip-iot.md
A SemanticTag represents the topic or the type of a piece of information"""
class SemanticTag(object):
	name = None # the simple name
	si = [] #the subject identifiers
	id = None #the unique id
	def __init__(self, name, si):
		if name:
			self.name = name
		if type(si) is list:
			self.si = si
		else:
			self.si = [si] #The si attribute should always be a list, even if there is only one SI

	def __str__(self):
		return " [Name]: %s  [Si]: %s" %(self.name, self.si)

	def __eq__(self, other): #ovewrwrites the check for equality of this class
		for identifier in self.si:
			if (identifier in other.si): #at least one subject identifier has to be equal to the other si
				return True
		return False

class Topic(SemanticTag):
	sender = None
	def __init__(self, name, si, sender=None):
		SemanticTag.__init__(self, name, si)
		self.sender = []
		if sender:
			if type(sender) is list:
				for s in sender:
					self.sender.append(s)
			elif type(sender) is Sender:
				self.sender.append(sender)

	def __str__(self, sender=False):
		if sender:
			return " [Name]: %s  [Si]: %s [Sender]: %s" %(self.name, self.si, self.sender)
		else:
			return " [Name]: %s  [Si]: %s" %(self.name, self.si)
			
class Sender(SemanticTag):
	channels = None
	def __init__(self, name, si, channels=None):
		SemanticTag.__init__(self, name, si)
		self.channels = []
		if channels:
			self.channels.append(channels)

	def add_channel(self, type, addr, advanced=None):
		if (advanced != None):
			self.channels.append((type,addr, advanced))
		else:
			self.channels.append((type,addr))

	def __str__(self):
		return "[Name]: %s  [Si]: %s [channels]: %s" % (self.name, self.si, self.channels)
