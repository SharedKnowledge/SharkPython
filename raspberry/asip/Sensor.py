#!/usr/bin/python
# -*- coding: utf-8 -*-

from SemanticTag import *
from Payload import Measurement
from Enum import Sensors, Temperature
import inspect
class Sensor():
	payloads = []

	def __init__(self, name, sensor_typ, host):
		self.name = name
		self.sender = host
		self.sensor_type = sensor_typ


	def add_payload_type(self, typ, unit):
		self.payloads.append(Measurement(self.sender, typ, unit))

	def get_measurements(self, typ):
		measures = ""
		for m in self.payloads:
			if m.typ == typ:
				measures += m.values.__str__()
		return measures

	def get_last_measurement(self, typ):
		measures = ''
		for m in self.payloads:
			if m.typ.si == typ.si:
				return m.values[-1]

	def add_value(self, typ, value):
		for m in self.payloads:
			if m.topic.si == typ.si:
				m.add_value(value)

	def __str__(self, long=False):
		measures = ""
		for m in self.payloads:
			measures += m.__str__() + '\n'
		return measures

class DHT(Sensor):
	def __init__(self, name, host, unit):
		Sensor.__init__(self, name, "DHT", host)
		unit= unit.replace(' ','').upper()
		if unit == "C" or unit == "F":
			unit = '°' + unit
		self.temp = Topic("Temperature"," Temp-SI", host)
		self.humi = Topic("Humidity","Humidity-SI", host)
		self.hIndex = Topic("Heat Index","HIndex-Si", host)
		self.add_payload_type(self.temp, unit)
		self.add_payload_type(self.humi, '%')
		self.add_payload_type(self.hIndex, unit)

	def add_temp(self, value):
		self.add_value(self.temp, value)

	def add_humidity(self, value):
		self.add_value(self.humi, value)

	def add_heat_index(self, value):
		self.add_value(self.hIndex, value)

		