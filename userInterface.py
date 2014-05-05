#!/usr/bin/env Python3

import sys

print ('\n')
print ("Welcome to the world.  Here you must clean the world of monsters.  Each monster will have a weapon on varying power.  Take care, as the monster might have more strength than you.  Remember retreat is a viable option.")

print ('\n')

class UI:
	#Initialize monsters
	monsterEngaged = False
	command = input("Please enter one of the following commands: monster, attack, defend, retreat, pick up,  help, stats.  The help command lists what each command does.  ")
	print ("To quit type: quit")
	while command != "quit":
		print ('\n')
		if command == "monster":
			if monsterEngaged == False:
				print ("You are now engaged with this monster:")
				print ("Name: ", '\n')
				print ("Health: ", '\n')
				print ("Weapon: ", '\n')
				monsterEngaged = True
				#Call function to engage monster
			else:
				print ("You are already engaged with a monster.  Please enter a new command.", '\n')
		elif command == "attack":
			if monsterEngaged == False:
				print("You are not engaged with a monster. Enter a new command.", '\n')
			else:
				#Call attack function
				print ("Your health, monster health", '\n')
		elif command == "defend":
			if monsterEngaged == False:
				print ("You are not engaged with a monster. Enter a new command.", '\n')
			else:
				#Call defend function
				print ("SHIELD SHIELD!", '\n')
		elif command == "retreat":
			if monsterEngaged == False:
				print("You are not engaged with a monster. Please enter a new command", '\n')
			else:
				#Call disengage function
				monsterEngaged = False
				print ("There is honor in retreat...Maybe", '\n')
		elif command == "stats":
			print ("Your health: ", '\n')
			print ("Your weapon: ", '\n')
			if monsterEngaged == True:
				print ("Monster's Health: ", '\n')
				print ("Monster's Weapon: ", '\n')
		elif command == "help":
			print ("monster    - engages a monster in combat", '\n')
			print ("attack     - attacks the monster", '\n')
			print ("defend     - defends against the monster's next attack", '\n')
			print ("retreat    - retreats from the monster you are attacking", '\n')
			print ("help       - displays commands", '\n')
			print ("stats - displays your statistics and those of the monster you are currently fighting", '\n')
			print ("pick up    - picks up the defeated monster's weapon", '\n')
			print ("quit       - exits the game", '\n')
		elif command == "pick up":
			print ("You now have this weapon", '\n')
		else:
			print (command)
		
		command = input("Command:   ")
	
	#If command = monster go to first monster in the list

	#if command = attact, defend, retreat

	#if monster is dead, ask to pick up weapon?
