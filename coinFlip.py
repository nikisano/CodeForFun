#!/usr/bin/python
import math
import random
#Nicholas Cipriano 8/14
#Mastemind Game written in Python

#function that randomly flips a coin and prints the percentage of heads and tails flips
def flipCoin(flips):
	heads = 0
	tails = 0
	totalflips = flips
	#loop untill the user input number of flips is hit
	while (flips > 0):
		#randomly flip the coin either a 0 or a 1 (heads or tails)
		coinflip=random.randint(0,1)
		if coinflip==0:
			heads=heads+1
		else:
			tails=tails+1
		flips=flips-1
	#Calculate percentages of head and tails flips
	headsPercent=((heads/totalflips)*100)
	tailsPercent=((tails/totalflips)*100)
	#Print out information on the flips
	print("You got ", headsPercent,"% heads" , " and ", tailsPercent, "% tails during the", totalflips, "flips")

#The codebreaker inputs their guess.  It must match te criteria of length 4 and 4 integers between 0 and 5
def numOfFlips():
	#variable is flipped when an integer is input by the user
	acceptableInput = 0
	#Loop untill we get a Guess that is an integer
	while(acceptableInput==0):
		try:
			totalflips = int(input("Enter the number of coins to flip: " ))
		#If we do not get an int we will get a value error and we will continue to loop untill we get an int input
		except ValueError:
			print ("Only Integers accepted.  Please try again.")
			acceptableInput = 0
		#When we get an int pass input to flip funciton
		else:
			totalflips=int(totalflips)
			acceptableInput = 1
			flipCoin(totalflips)

#call function that takes input number of flips from user
numOfFlips()