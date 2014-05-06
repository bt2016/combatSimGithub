#!/usr/bin/env python3

import sys
from random import randint

from record_jar_reader import record_jar_reader
test = record_jar_reader()
test.loadFiles('data.rjar', 'weapons.rjar')
monsters = test.getMonsters()
weapons = test.getWeapons()


print ('\n')
print ("Welcome to the world.  Here you must clean the world of monsters.  Each monster will have a weapon of varying power.  Take care, as the monster might have more strength than you.  Remember retreat is a viable option.")

print ('\n')

weapon = randint(0,4)
#yourWeapon = dict[weapon]
yourWeaponDict = weapons[weapon]
yourWeapon = yourWeaponDict['Name']
yourHealth = 20
yourAttack = yourWeaponDict['Attack']
num = randint(0,4)
currentMonsterDict = monsters[num]
monterName = currentMonsterDict['Name']

print ("Your weapon: ", yourWeapon, '\n')
print ("Your attack: ", yourAttack, '\n')

#monster call list entry return dict
currentMonster = monsters[num]
#weapons call list entry return dict

#Initialize monsters
monsterEngaged = False
monsterDead = False
MonsterCount = 0
gameOver = False
nextMonster = True
newHealth = int(yourHealth)
command = input("Please enter one of the following commands: monster, attack, defend, retreat, pick up,  help, stats.  The help command lists what each command does. To quit, type quit \n")

while command != "quit":
	print ('\n')
	if command == "monster":#Engages the monster
		if monsterEngaged == False:
			if nextMonster == True:
				num = randint(0,4)
				currentMonsterDict = monsters[num]
				monsterName = currentMonsterDict['Name']
				monsterHealth = currentMonsterDict['Health']
				monsterAttack = currentMonsterDict['Attack']
				nextMonster = False
				newMonsterHealth = int(monsterHealth)
				weapon2 = randint(0,4)
				monstWeap = weapons[weapon2]
				monsterWeapon = monstWeap['Name']
			print ("You are now engaged with this monster:", '\n')
			print ("Name: ", monsterName, '\n')
			print ("Health: ", monsterHealth, '\n')
			print ("Attack: ", monsterAttack, '\n')
			print ("Weapon: ", monsterWeapon, '\n')
			monsterEngaged = True
			monsterDead = False
			#Call function to engage monster
		else:
			print ("You are already engaged with a monster.  Please enter a new command.", '\n')
	elif command == "attack": #Attacks the monster unless not engaged with one
		if monsterEngaged == False:
			print("You are not engaged with a monster. Enter a new command.", '\n')
		else:
			#Call attack function
			#Sample attack
			newHealth = newHealth - int(monsterAttack)
			newMonsterHealth = newMonsterHealth - int(yourAttack)
			print ("Your health: ", newHealth, '\n')
			print ("Monster health: ", newMonsterHealth, '\n')
			if newMonsterHealth <=0:
				monsterDead = True
				monsterEngaged = False
				nextMonster = True
				print("You killed the monster", '\n')
			if newHealth <= 0:
				print ("You died, please try again", '\n')
				gameOver = True
	elif command == "defend": #Defends against the monster's attack unless not engaged with one
		if monsterEngaged == False:
			print ("You are not engaged with a monster. Enter a new command.", '\n')
		else:
			#Call defend function
			#Sample defend
			mod = randint(-10,10)
			if mod == 0:
				mod = 0.10
			mod2 = 1/mod
			newHealth -= mod2*int(monsterAttack)
			print ("SHIELD SHIELD!", '\n')
			print ("Your health: ", newHealth, '\n')
			print ("Monster health: ", newMonsterHealth, '\n')
			if newHealth <= 0:
				print ("You died, please try again", '\n')
				gameOver = True
	elif command == "retreat": #Retreats from the battle
		if monsterEngaged == False:
			print("You are not engaged with a monster. Please enter a new command", '\n')
		else:
			#Call disengage function
			monsterEngaged = False
			print ("When you fight and run away....You live to fight another day.", '\n')
	elif command == "stats": #Displays your health and weapon, and if you are fighting a monster, displays its health and weapon
		print ("Your health: ", newHealth, '\n')
		print ("Your weapon: ", yourWeapon, '\n')
		print ("Your attack: ", yourAttack, '\n')
		if monsterEngaged == True:
			print ("Monster's Name:   ", monsterName, '\n')
			print ("Monster's Health: ", newMonsterHealth, '\n')
			print ("Monster's Attack: ", monsterAttack, '\n')
	elif command == "help":#Outputs all of the commangs and what they do
		print ("monster    - engages a monster in combat", '\n')
		print ("attack     - attacks the monster", '\n')
		print ("defend     - defends against the monster's next attack", '\n')
		print ("retreat    - retreats from the monster you are attacking", '\n')
		print ("help       - displays commands", '\n')
		print ("stats      - displays your statistics and those of the monster you are currently fighting", '\n')
		print ("pick up    - picks up the defeated monster's weapon", '\n')
		print ("quit       - exits the game", '\n')
	elif command == "pick up":#Also need to scheck if monster is dead
		if monsterEngaged == True:
			print ("The monster is not yet dead so there is no weapon to pick up.", '\n')
		elif monsterDead == True:
				print ("You now have this weapon: ", monsterWeapon, '\n')
				yourWeapon = monsterWeapon
				yourAttack = monstWeap['Attack']
		else:
			print ("You are not engaged with a monster.", '\n')
	elif command == "What is the answer to life, the universe, and everything?":
		print ("42", '\n')
	else:
		print ("Invalid Command.  Please use: monster, attack, defend, retreat, help, stats, pick up, or quit", '\n')
	
	if gameOver == True:
		command = "quit"
	else:
		command = input("Command:   ")

