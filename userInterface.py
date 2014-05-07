#!/usr/bin/env python3

import sys
from random import randint
from math import floor
import Ent

from record_jar_reader import record_jar_reader
test = record_jar_reader()
test.loadFiles('data.rjar', 'weapons.rjar')
monsters = test.getMonsters()
weapons = test.getWeapons()

currentMonster = Ent.Monster()
currentWeapon = Ent.Item()
print ('')
print ("Welcome to the world.  Here you must clean the world of monsters.  Each monster will have a weapon of varying power.  Take care, as the monster might have more strength than you.  Remember retreat is a viable option.")

print ('\n')

weapon = randint(0,4)
#yourWeapon = dict[weapon]
yourWeaponDict = weapons[weapon]
yourCurrentWeapon = Ent.GenWeapon(yourWeaponDict)

name = input("What would you like to be called?: ")
if name == '':
	name = 'Player'
player = Ent.GenPlayer(name, 20, 5)

num = randint(0,4)

print ("You are: ")
print (player)

#weapons call list entry return dict
monsterDied = 0
#Initialize monsters
monsterEngaged = False
monsterDead = False
MonsterCount = 0
gameOver = False
nextMonster = True
retreatVal = 0
pickUp = False
print ("Please enter one of the following commands: monster, attack, defend, retreat, pick up,  help, stats.  The help command lists what each command does. To quit, type quit")
print ("To engage a monster, type monster",'\n')
command = input("Command:    ")
commandList = command.split()
command = commandList[0]
while command != "quit":
	if command == "monster":#Engages the monster
		if monsterEngaged == False:
			if nextMonster == True:
				if monsterDied > 4:
					num = randint(0,4)
				else:
					num = randint(0, monsterDied)
				currentMonsterDict = monsters[num]
				currentMonster = Ent.GenMonster(currentMonsterDict)
				nextMonster = False

				wepChance = randint(0, 100)
				if wepChance <= (10 * (num + 1)):
					weapon2 = randint(0,4)
					Ent.GiveItem(currentMonster, Ent.GenWeapon(weapons[weapon2]))
			print ("You are now engaged with this monster:")
			print (currentMonster)
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

#			newHealth = newHealth - int(monsterAttack)
#			newMonsterHealth = newMonsterHealth - int(yourAttack)
#			print ("Your health: ", newHealth)
#			print ("Monster health: ", currentMonster.HP)
#			if currentMonster.HP <=0:

			Ent.Attack(player, currentMonster)
			
			# Monster performs a random action
			monsterAction = randint(0, 2)
			if currentMonster.HP > 0:
				if monsterAction == 0:
					Ent.Attack(currentMonster, player)
				elif monsterAction == 1:
					Ent.Defend(currentMonster)
				elif monsterAction == 2:
					Ent.Focus(currentMonster)
			else:
				print(currentMonster.name + " breathes its last!")
			if currentMonster.HP <= 0:
				monsterDead = True
				monsterEngaged = False
				monsterDied +=1
				nextMonster = True
				print("You killed the monster")
				if len(currentMonster.inventory) > 0:
					print("\nThe monster dropped ", currentMonster.inventory[0])
					ans = input("Pick it up? (Y/N): ")
					while ans != 'y' and ans != 'Y' and ans != 'N' and ans != 'n':
						input("Invalid answer, Pick it up? (Y/N)")
					if ans == 'y' or ans == 'Y':
						Ent.GiveItem(player, currentMonster.inventory[0])
					elif ans == 'n' or ans == 'N':
						print("You leave the item and move on")
			if player.HP <= 0:
				gameOver = True
	elif command == "defend": #Defends against the monster's attack unless not engaged with one
		if monsterEngaged == False:
			print ("You are not engaged with a monster. Enter a new command.")
		else:
			#Call defend function
			#Sample defend

#			mod = randint(-10,10)
#			if mod == 0:
#				mod = 0.10
#			mod2 = 1/mod
#			newHealth -= mod2*int(currentMonster.ATK)
#			print ("SHIELD SHIELD!")
#			print ("Your health: ", newHealth)
#			print ("Monster's Health: ", currentMonster.HP)
#			if newHealth <= 0:

			Ent.Defend(player)

			monsterAction = randint(0, 2)
			if monsterAction == 0:
				Ent.Attack(currentMonster, player)
			elif monsterAction == 1:
				Ent.Defend(currentMonster)
			else:
				Ent.Focus(currentMonster)

			if player.HP <= 0:
				gameOver = True
	elif command == "focus":
		if monsterEngaged == False:
			print("You are not engaged with a monster. Enter a new command.")
		else:
			Ent.Focus(player)
	
			monsterAction = randint(0,2)
			if monsterAction == 0:
				Ent.Attack(currentMonster, player)
			elif monsterAction == 1:
				Ent.Defend(currentMonster)
			else:
				Ent.Focus(currentMonster)

			if player.HP <= 0:
				gameOver = True
	elif command == "retreat": #Retreats from the battle
		if retreatVal <= 1:
			if monsterEngaged == False:
				print("You are not engaged with a monster. Please enter a new command")
			else:
				retreatVal += 1
				#Call disengage function
				monsterEngaged = False
				Ent.Heal(player, floor(player.Max_HP / 10))
				print ("When you fight and run away....You live to fight another day.")
		else:
			if monsterEngaged == False:
				print ("You are not engaged with a monster.  Please enter a new command")
			else:
				print ("You have used up all your retreats... No cowards allowed")
	elif command == "stats": #Displays your health and weapon, and if you are fighting a monster, displays its health and weapon
		print (player)
		if monsterEngaged == True:
			print ("You are currently fighting:\n" + str(currentMonster))
	elif command == "help":#Outputs all of the commangs and what they do
		print ("monster    - engages a monster in combat")
		print ("attack     - attacks the monster")
		print ("defend     - defends against the monster's next attack")
		print ("retreat    - retreats from the monster you are attacking")
		print ("help       - displays commands")
		print ("stats      - displays your statistics and those of the monster you are currently fighting")
		print ("pick up    - picks up the defeated monster's weapon")
		print ("quit       - exits the game")
	elif " ".join(commandList) == "What is the answer to life, the universe, and everything?":
		print ("42")
	elif command == "inventory":
		player.PrintInventory()
	elif command == "equip":
		if len(player.inventory) == 0:
			print ("You don't have anything to equip!")
		else:
			if len(commandList) < 2:
				try:
					slot = int(input("Which slot would you like to equip?: "))
				except ValueError:
					slot = -1
				Ent.EquipItem(player, slot)
			else:
				try:
					slot = int(commandList[1])
				except ValueError:
					slot = -1
				Ent.EquipItem(player, slot) 
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
		commandList = command.split()
		command = commandList[0]

