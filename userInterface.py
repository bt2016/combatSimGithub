#!/usr/bin/env python3

import sys
from random import randint

print ('\n')
print ("Welcome to the world.  Here you must clean the world of monsters.  Each monster will have a weapon on varying power.  Take care, as the monster might have more strength than you.  Remember retreat is a viable option.")

print ('\n')

weapon = randint(0,4)
#yourWeapon = dict[weapon]
yourWeapon = "Great Sword"
yourHealth = 20
for i in range(0,4):
	num = randint(0,4)


#Initialize monsters
monsterEngaged = False
monsterDead = False
MonsterCount = 0
gameOver = False
command = input("Please enter one of the following commands: monster, attack, defend, retreat, pick up,  help, stats.  The help command lists what each command does. To quit, type quit \n")
while command != "quit":
	print ('\n')
	if command == "monster":#Engages the monster
		if monsterEngaged == False:
			print ("You are now engaged with this monster:", '\n')
			print ("Name: ", '\n')
			print ("Health: ", '\n')
			print ("Weapon: ", '\n')
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
			print ("Your health: ", yourHealth, '\n')
			print ("Monster health: ", '\n')
	elif command == "defend": #Defends against the monster's attack unless not engaged with one
		if monsterEngaged == False:
			print ("You are not engaged with a monster. Enter a new command.", '\n')
		else:
			#Call defend function
			print ("SHIELD SHIELD!", '\n')
			print ("Your health: ", yourHealth, '\n')
			print ("Monster health: ", '\n')
	elif command == "retreat": #Retreats from the battle
		if monsterEngaged == False:
			print("You are not engaged with a monster. Please enter a new command", '\n')
		else:
			#Call disengage function
			monsterEngaged = False
			print ("When you fight and run away....You live to fight another day.", '\n')
	elif command == "stats": #Displays your health and weapon, and if you are fighting a monster, displays its health and weapon
		print ("Your health: ", yourHealth, '\n')
		print ("Your weapon: ", yourWeapon, '\n')
		if monsterEngaged == True:
			print ("Monster's Health: ", '\n')
			print ("Monster's Weapon: ", '\n')
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
				print ("You now have this weapon", '\n')
		else:
			print ("You are not engaged with a monster.", '\n')
	elif command == "What is the answer to life, the universe, and everything?":
		print ("42", '\n')
	else:
		print ("Invalid Command.  Please use: monster, attack, defend, retreat, help, stats, pick up, or quit", '\n')
	
	command = input("Command:   ")
	if gameOver == True:
		command = "quit"
