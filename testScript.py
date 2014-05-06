#!/usr/bin/env python3

#from record_jar_reader import load_records
#rooms = load_records( open('data.rjar', 'r') )
#from pprint import pprint #to pretty-print Python objects
#pprint(rooms)
#rooms is a list of dictionaries

#import record_jar_reader as getData
#test = getData.loadFiles('data.rjar', 'weapons.rjar')
#from pprint import pprint
#pprint(test.getMonsters())




from record_jar_reader import record_jar_reader
test = record_jar_reader()
test.loadFiles('data.rjar', 'weapons.rjar')
monsters = test.getMonsters()
weapons = test.getWeapons()
from pprint import pprint
pprint(monsters)
pprint(weapons)


