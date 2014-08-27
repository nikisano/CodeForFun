#!/usr/bin/python
import random
#Nicholas Cipriano 8/14
#Mastemind Game written in Python

#create variable to see how many guesses have been used
guessNum = 1

#create the code that needs to be broken random int from 0 to three in 4 locations
def codeMaker():
	slot1 = random.randint(0,5)
	slot2 = random.randint(0,5)
	slot3 = random.randint(0,5)
	slot4 = random.randint(0,5)
	solution = [slot1, slot2, slot3, slot4]
	return solution

#The codebreaker inputs their guess.  It must match te criteria of length 4 and 4 integers between 0 and 5
def codeBreaker(guessNum):
	goodGuess = 0
	#Loop untill we get a Guess that matches our needs
	while(goodGuess==0):
		guess = input('Enter your %s guess at the code:'%(guessNum))
		if (len(guess) != 4):
			print ('Your code was the incorrect length.  Retry.')
		elif (int(guess[0])>6 or int(guess[1])>6 or int(guess[2])>6 or int(guess[3])>6):
			print('You must use numbers 0 through 5.  Retry.')
		else:
			goodGuess = 1
			return guess

#test guess versus computer generated code and return correct spot and correct number
def testCode(solution, guessNum):
	#user gets 10 guesses to get it right
	while(guessNum<10):
		#need list(solutions) if you set it equal just to the list it is just a differint ID tag to the same list
		checkGuess = list(solution)
		#variable if the number is in the correct spot
		rightSpot = 0
		#variable if the number is in the code but in the wrong spot
		rightNumWrongSpot = 0
		count = 0 
		#retrieve the user input guess
		guess = codeBreaker(guessNum)
		#loop to see if the guess is correct or if anything in the guess was correct
		for i in guess:
			if (int(i)==checkGuess[count]):
				rightSpot=rightSpot+1
				checkGuess[count] = 'x'
			elif(int(i) == checkGuess[0]):
				checkGuess[0]= 'x'
				rightNumWrongSpot = rightNumWrongSpot + 1
			elif(int(i) == checkGuess[1]):
				checkGuess[1]= 'x'
				rightNumWrongSpot = rightNumWrongSpot + 1
			elif(int(i) == checkGuess[2]):
				checkGuess[2]= 'x'
				rightNumWrongSpot = rightNumWrongSpot + 1
			elif(int(i) == checkGuess[3]):
				checkGuess[3]= 'x'
				rightNumWrongSpot = rightNumWrongSpot + 1
			count = count +1
		#if all 4 are in the right spot you win the game
		if(rightSpot==4):
			print('You win the game in', guessNum, 'Guesses')
			break
		#If not print the results and continue on untill 10 guesses are up
		else:
			guessNum=guessNum+1
			print ('your guess has', rightSpot, 'in the correct spot and',rightNumWrongSpot, 'with the right number in the wrong spot')
	if (guessNum==10):
		print("You lost the game after 10 guesses you did not get the code.")
		print("The Correct code was", solution)
		
testCode(codeMaker(),guessNum)
