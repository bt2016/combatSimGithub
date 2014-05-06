#!/usr/bin/env python3

class record_jar_reader:
	
	def __init__(self):
		self.monsters = {}
		self.weapons = {}

	def loadFiles(self, file1, file2):
		self.monsters = self.load_records( open('data.rjar', 'r') )
		self.weapons = self.load_records( open('weapons.rjar', 'r') )


	def record_reader(self,flo):
        	record = {}
       		for line in flo:
                	if line.startswith('%%'):
                        	yield record
	                        record = {}
                	else:
                        	key, value = line.split(':')
                        	record[key.strip()] = value.strip()
                        
        	yield record

	def load_records(self,flo):
		return [ record for record in self.record_reader(flo) ]

	def printMonsters(self):
		from pprint import pprint
		pprint(self.monsters)

	def getMonsters(self):
		return self.monsters

	def getWeapons(self):
		return self.weapons
