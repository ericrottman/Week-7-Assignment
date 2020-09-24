# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <author>
# Creation Date: <date>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight./n''') #used /n to create blank line instead of empty print()
	# print()

def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()

	# return caves
	return cave  #cave needs to be singular to match the previous variable that was set

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	# time.sleep(3)
	time.sleep(2) #sleep time was previously set to 3 seconds not 2
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		# print 'Gobbles you down in one bite!'
		print('Gobbles you down in one bite!')  # print statement needs parentheses

# playAgain = 'yes'
# while playAgain == 'yes' or playAgain == 'y':
# 	displayIntro()
# 	caveNumber = choosecave()
# 	checkCave(caveNumber)
# 	print('Do you want to play again? (yes or no)')
# 	playAgain = input()
# 	if playAgain == "no":
# 		print("Thanks for planing")
# 	#add elif for if playAgain = yes
# 	elif playAgain == 'yes' or playAgain == 'y':
# 		playAgain()

#make entire playAgain into function to allow for proper looping
def again():
	playAgain = 'yes'
	# while playAgain = 'yes' or playAgain = 'y':
	while playAgain == 'yes' or playAgain == 'y': #needs 2 "=" to be used for comparision
		displayIntro()
		# caveNumber = choosecave()
		caveNumber = chooseCave() #"C" in cave of chooseCave needs to be capitalized to match the defined function
		checkCave(caveNumber)
		print('Do you want to play again? (yes or no)')
		playAgain = input()
		if playAgain == "no":
			# print("Thanks for planing")
			print("Thanks for playing") #typo of planing corrected to playing
			break #break needed to be called to end the program
		# add elif for if playAgain = yes
		elif playAgain == 'yes' or playAgain == 'y':
			again()

again() #function needs to be called to start the program