#!/usr/bin/env python3

import sys
from random import randint

from record_jar_reader import record_jar_reader
test = record_jar_reader()
test.loadFiles('data.rjar', 'weapons.rjar')
monsters = test.getMonsters()
weapons = test.getWeapons()


print ('')
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

print ("Health:      ", yourHealth)
print ("Your weapon: ", yourWeapon)
print ("Your attack: ", yourAttack)
print ('')

#monster call list entry return dict
currentMonster = monsters[num]
#weapons call list entry return dict
monsterDied = 0
#Initialize monsters
monsterEngaged = False
monsterDead = False
MonsterCount = 0
gameOver = False
nextMonster = True
newHealth = int(yourHealth)
retreatVal = 0
print ("Please enter one of the following commands: monster, attack, defend, retreat, pick up,  help, stats.  The help command lists what each command does. To quit, type quit")
print ("To engage a monster, type monster")
command = input("Command:    ")
while command != "quit":
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
			print ("You are now engaged with this monster:")
			print ("Name: ", monsterName)
			print ("Health: ", monsterHealth)
			print ("Attack: ", monsterAttack)	
			monsterEngaged = True
			monsterDead = False
			#Call function to engage monster
		else:
			print ("You are already engaged with a monster.  Please enter a new command.")
	elif command == "attack": #Attacks the monster unless not engaged with one
		if monsterEngaged == False:
			print("You are not engaged with a monster. Enter a new command.")
		else:
			#Call attack function
			#Sample attack
			newHealth = newHealth - int(monsterAttack)
			newMonsterHealth = newMonsterHealth - int(yourAttack)
			print ("Your health: ", newHealth)
			print ("Monster health: ", newMonsterHealth)
			if newMonsterHealth <=0:
				monsterDead = True
				monsterEngaged = False
				monsterDied +=1
				nextMonster = True
				print("You killed the monster")
				print("The monster dropped this weapon: ", monsterWeapon, "  It has an attack of ", monstWeap['Attack'], "  To pick up, type pick up")
			if newHealth <= 0:
				gameOver = True
	elif command == "defend": #Defends against the monster's attack unless not engaged with one
		if monsterEngaged == False:
			print ("You are not engaged with a monster. Enter a new command.")
		else:
			#Call defend function
			#Sample defend
			mod = randint(-10,10)
			if mod == 0:
				mod = 0.10
			mod2 = 1/mod
			newHealth -= mod2*int(monsterAttack)
			print ("SHIELD SHIELD!")
			print ("Your health: ", newHealth)
			print ("Monster health: ", newMonsterHealth)
			if newHealth <= 0:
				gameOver = True
	elif command == "retreat": #Retreats from the battle
		if retreatVal <= 1:
			if monsterEngaged == False:
				print("You are not engaged with a monster. Please enter a new command")
			else:
				retreatVal += 1
				#Call disengage function
				monsterEngaged = False
				if newHealth <= 20:
					newHealth += (newHealth/2)
					if newHealth >20:
						newHealth = 20
				print ("When you fight and run away....You live to fight another day.")
		else:
			if monsterEngaged == False:
				print ("You are not engaged with a monster.  Please enter a new command")
			else:
				print ("You have used up all your retreats... No cowards allowed")
	elif command == "stats": #Displays your health and weapon, and if you are fighting a monster, displays its health and weapon
		print ("Your health: ", newHealth)
		print ("Your weapon: ", yourWeapon)
		print ("Your attack: ", yourAttack)
		if monsterEngaged == True:
			print ("Monster's Name:   ", monsterName)
			print ("Monster's Health: ", newMonsterHealth)
			print ("Monster's Attack: ", monsterAttack)
	elif command == "help":#Outputs all of the commangs and what they do
		print ("monster    - engages a monster in combat")
		print ("attack     - attacks the monster")
		print ("defend     - defends against the monster's next attack")
		print ("retreat    - retreats from the monster you are attacking")
		print ("help       - displays commands")
		print ("stats      - displays your statistics and those of the monster you are currently fighting")
		print ("pick up    - picks up the defeated monster's weapon")
		print ("quit       - exits the game")
	elif command == "pick up":#Also need to scheck if monster is dead
		if monsterEngaged == True:
			print ("The monster is not yet dead so there is no weapon to pick up.")
		elif monsterDead == True:
				print ("You now have this weapon: ", monsterWeapon)
				yourWeapon = monsterWeapon
				yourAttack = monstWeap['Attack']
		else:
			print ("You are not engaged with a monster.")
	elif command == "What is the answer to life, the universe, and everything?":
		print ("42")
	else:
		print ("Invalid Command.  Please use: monster, attack, defend, retreat, help, stats, pick up, or quit")
	
	if gameOver == True:
		print('\n')
		print ("You died, please try again")
		print("You killed ", monsterDied, "monsters")
		command = "quit"
	else:
		print ('')
		command = input("Command:   ")

