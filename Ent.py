#!/usr/bin/env python3

from math import floor
from random import randint

# Messages for certain status effects ocurring
StatusMessages = {
"FOCUS": " aims carefully!",
"DEFEND": " defends!"
}

StatusTypes = ["ATK_BUFF", "DEF_BUFF", "DOT"]

class Status:
	# Defines a status effect
	def __init__(self, type, name, modifier):
		if type in StatusTypes:
			self.type = type
			self.name = name
			self.modifier = modifier
			self.lifeTime = 0
	def setLife(self, life):
		self.lifeTime = life

# Performs an attack calculation
def Attack(source, target):
	# Start with base multiplier of 1
	ATK_Multiplier = 1
	# Add positive attack modifiers (ATK_BUFFs)
	for status in source.status:
		if status.type is "ATK_BUFF":
			# Decrements lifetime counter for the buff, or removes it if it has timed out
			if status.lifeTime == 0:
				(source.status).remove(status)
			else:
				status.lifeTime -= 1

			# Prints out the buff's message
			print(str(source.name) + StatusMessages[status.name])
			ATK_Multiplier += status.modifier
	# Checks for negative attack modifiers (DEF_BUFFs)
	for status in target.status:
		if status.type is "DEF_BUFF":
			ATK_Multiplier -= status.modifier
			if status.lifeTime == 0:
				(source.status).remove(status)
			else:
				status.lifeTime -= 1
			print(str(target.name) + StatusMessages[status.name])
	trueATK = source.ATK
	# Checks for equipped items in invenntory, adds them to base attack if equipped
	#	and they have an ATK modifier
	try:
		for item in source.inventory:
			if item.equipped == 1:
				trueATK += item.ATK
	# Softly fails if they don't have an ATK modifier
	except AttributeError:
		pass

	# Generates random number from 0 to trueATK, multiplies by the attack modifier
	damage = floor(randint(0, trueATK) * ATK_Multiplier)
	
	# Seperate message for no damage
	if damage <= 0:
		print(str(target.name) + " takes no damage")
	# Otherwise prints out how much damage was dealth, decrements target HP
	else:
		print(str(target.name) + " is hit for " + str(damage) + " points of damage")
		target.HP -= damage
	return

# Applies the DEFEND status effect on the given ENT
def Defend(source):
	# Checks to see if the ENT is already defending first
	if not any(status.name == "DEFEND" for status in source.status):
		# Prints message, applies status effect	
		print(str(source.name) + " braces for the next attack!")
		(source.status).append(Status("DEF_BUFF", "DEFEND", 0.75))
	else:
		print(str(source.name) + " continues defending")

# Applies the FOCUS status effect on the given ENT
def Focus(source):
	# If not already focused, adds the effect w/ a 25% strength
	if not any(status.name == "FOCUS" for status in source.status):
		(source.status).append(Status("ATK_BUFF", "FOCUS", 0.25))
		print(str(source.name) + " begins focusing!")
	else:
		# Otherwises find it and increases its strength
		for status in source.status and status.name == "FOCUS" and status.modifier < 1.5:
			# Buff gets stronger the more times it is applied
			#	starting at 25%, then 50%, then 150%
			status.modifier += status.modifier / 0.5
			print(str(source.name) + " intensifies their focus!")
		else:
			# If buff is already at max strength, say so
			print(str(source.name) + " can't focus any harder!")

class Monster:
	def __init__(self):
		self.name = ""
		self.Max_HP = 0
		self.HP = 0
		self.ATK = 0
		self.status = []
		self.actions = []
		self.inventory = []
		self.alignment = []

class Player:
	def __init__(self):
		self.name = "Player"
		self.Max_HP = 0
		self.HP = 0
		self.ATK = 0
		self.status = []
		self.actions = []
		self.inventory = []

