from SemanticTag import *
from Exceptions import *
from Sensor import *
class AsipKnowledge(object):
	# bekannte Sender
	sender = None
	# bekannte Topic
	topics = None
	# gespeicherte Payloads
	payloads = None

	def __init__(self, host):
		self.topics = []
		self.sender = []
		self.host = None
		self.payloads = []
		if isinstance(host, Sender):
			self.sender.append(host)
			self.host = host
		else:
			raise TypeError("sender", "Sender")

	''' Jede Strucutr mit einem "payloads" Attribut, kann gemerged werden 
	'''
	def merge(self, strucutre):
		if hasattr(strucutre, 'payloads'):
			for pl in strucutre.payloads:
				self.add_payload(pl)

	'''Payload hinzufuegen
		Wenn Topic unbekannt - Topic hinzufuegen
		Wenn values teilweise bekannt sind, ueberschreiben die neuen values diese
	'''
	def add_payload(self, payload):
		si_matches = filter(lambda x: x.topic.si==payload.topic.si, self.payloads)
		matches = len(si_matches)
		for pl in si_matches:
			(same, new) = payload.same_as(pl)
			if new:
				pl.values = payload.values
				break
		if (matches > 0):
			self.topics.append(payload.topic)
		self.payloads.append(payload)

	''' Filtert die Inhalte der KB nach einem Topic
	
		if (values == True) : liefert (Topics, Sender, values) 
		else				: liefert (Topics, Sender)

	''' 
	def by_si(self, topic, values=True):
		topic_sis = map(lambda x: x.si, self.topics)
		topic_matches = filter(lambda x: x==(topic.si), topic_sis)
		sender_matches = []
		for t in topic_matches:
			if type(t.sender) is list:
				for s in t.sender:
					sender_matches.append(s)
			else:
				sender_matches.append(t.sender)
		if values:
			value_sis = map(lambda x: x.topic.si, self.payloads)
			value_matches = filter(lambda x: x==(topic.si), value_sis)
			return (topic_matches, sender_matches, value_matches)
		else:
			return  (topic_matches, sender_matches)
	
	''' Erstellt einen neuen DHT-Sensor und updated ggf. eigene Topics 
	'''
	def new_dht(self, name, unit):
		dht = DHT(name, self.host, unit)
		for m in dht.payloads:
			self.add_topic(m.topic)
		return dht

	def new_topic (self, name, si, sender=None):
		pass

	''' Liefer True, falls das Topic neu ist,
		ansonsten False
	'''
	def is_new_si(self, topic):
		sis = map(lambda x: x.si, self.topics)
		matches = filter(lambda x: x==(topic.si), sis)
		if matches and len(matches) > 0:
			return False
		else:
			return True

	''' Liefer True, falls der Name neu ist,
		ansonsten False
	'''
	def is_new_name(self, topic):
		matches = []
		names = map(lambda x: x.name, self.topics)
		matches = filter(lambda x: x==(topic.name), names)
		if len(matches) == 0:
			return True
		else:
			return False

	''' Fuegt Topic (wenn neu) zur KB hinzufuegen

		Ansonsten IdentificationsError
	'''
	def add_topic(self, topic):
		si_new = self.is_new_si(topic)
		name_new = self.is_new_name(topic)
		if name_new and si_new:
			self.topics.append(topic)
		else:
			raise IdentificationsError(si_known, name_known)

	''' Erlaubt das suche von Topics

		Wenn Topic bekannt, wird dieses zurueckgegeben
	'''
	def get_topic(self, topic):
		si = topic.get_si()
		topic_si = (filter(lambda x: x.get_si() == si, self.topics))
		if len(topic_si) == 1:
			return topic_si[0]


	def __str__(self):
		info = ""
		if len(self.topics) > 0:
			info += "[Topics]:\n"
			for t in self.topics:
				info += "\t %s \n" % (t.__str__())
			info += "\n"
		if len(self.sender) > 0:
			info += "[Sender]:\n"
			for s in self.sender:
				info += "\t%s" % (s.__str__())
			info += "\n"
		if len(self.payloads) > 0:
			info += "[Payloads]:\n"
			for p in self.payloads:
				info += "\t%s\n" % (p.__str__())
			info += "\n"
		return info


h = Sender("Sender1","asip/user123", ("BLE", "f8:bc:ac:12:1A"))
a = AsipKnowledge(h)
d = a.new_dht("BLE Sensor", 'C')
d.add_temp(17)
d.add_humidity(45)
d.add_heat_index(15)
a.merge(d)
print a.__str__()
