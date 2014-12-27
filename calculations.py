from random import randrange
from score_card import *

class dice():
	def roll(current_dice):
		while len(current_dice) != 5:
			current_dice.append(randrange(1,7))
		current_dice.sort()	
		return current_dice
	def turn(options, score):
		current_dice = []					
		print(dice.roll(current_dice))
		current_dice = dice.rolltwothree(current_dice)
		current_dice = dice.rolltwothree(current_dice)
		dice.rolltwothree(current_dice, options, score, 1)
	
	def rolltwothree(current_dice, options = 1, score = 1, last = 0):
		if last == 0:
			while True:
				#choice = input("You did not enter a valid respond your options are y or n: ")
				choice = input("Would you like to reroll some dice? y or n: ")
				if choice == "y":
					break
				elif choice == "n":
					break
			if choice == "y":
				while True:
					try:
						keep = input("Enter the number of each die you would like to keep with a comma between: ").split(",")
						if keep == ['']:
							keep = []
							break
						keep = [int(i) for i in keep]	#converts keep from a str into an int

						if (current_dice.count(1) >= keep.count(1) and
							current_dice.count(2) >= keep.count(2) and
							current_dice.count(3) >= keep.count(3) and
							current_dice.count(4) >= keep.count(4) and
							current_dice.count(5) >= keep.count(5) and
							current_dice.count(6) >= keep.count(6)):
								current_dice = keep
								break
						else:
							print("\nYou are trying to keep dice you don't have please try again.")
					except ValueError:
						print("\nYou did not follow the proper formatting please try again")
						continue
				current_dice = dice.roll(keep)
				print(current_dice)
				return current_dice	
			elif choice == "n":
				return current_dice
		else:
			score_card.selection(current_dice, options, score)