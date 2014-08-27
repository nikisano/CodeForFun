#!/usr/bin/python

import random
#Nicholas Cipriano 8/27
#Tic Tac Toe Game written in Python

def printInstructions():
	#Print Help instructions to make it clear where the X or O will be placed
	print("Welcome to Nicks simple version of Tic Tac Toe.  You can play versus the computer on easy or hard difficulty.  Select weather you would like to play as X or O.  Computer will randomly pick who will go first.  When it is your turn You will enter a number from 0 to 8 using the map below to select where you want to place your X or O.")
	print("\n0|1|2 \n_____\n3|4|5 \n_____\n6|7|8")

def userMenuSelect():
	#untill a X or a O is selected keep trying to recieve correct input from user
	userHasSelected=0
	userID = '*'

	while (userHasSelected==0):
		menuInput = input('Would you like to play as X or O?  type help for instructions: ')
		if(menuInput.lower()=='help'):
			printInstructions()
		elif(menuInput.lower()=='x'):
			userID='X'
			return userID
		elif(menuInput.lower()=='o'):
			userID='O'
			return userID
		else:
			print("The only acceptable inputs are X, O, and Help.  please try again")

def difficultyLevel():
	#untill e or h is selected keep trying to recieve correct input from user
	userHasSelected=0

	while (userHasSelected==0):
		difficultyLevelInput = input('Would you like to play on easy or hard difficulty?(E for easy level, H for hard level)')
		if(difficultyLevelInput.lower()=='help'):
			printInstructions()
		elif(difficultyLevelInput.lower()=='e'):
			difficulty=0
			return difficulty
		elif(difficultyLevelInput.lower()=='h'):
			difficulty=1
			return difficulty
		else:
			print("The only acceptable inputs are E, H, and Help.  please try again")

def firstMove():
	#Randomly generate a 0 or 1 to decide who will get the first move
	if (random.randint(0,1)==0):
		print("Computer gets first move")
		return 0
	else:
		print("You get first move")
		return 1

def printBoard():
	#print tic tac toe board.  board[] is a list of current played moves
	print('\n'+ board[0]+'|'+board[1]+'|'+board[2]+' \n_____\n'+board[3]+'|'+board[4]+'|'+board[5]+' \n_____\n'+board[6]+'|'+board[7]+'|'+board[8])

def checkWinner(checkBoard):
	#top wins if
	if(checkBoard[0]!='*' and checkBoard[0]==checkBoard[1] and checkBoard[1]==checkBoard[2]):
		return True
	#middle wins if
	elif(checkBoard[3]!='*' and checkBoard[3]==checkBoard[4] and checkBoard[4]==checkBoard[5]):
		return True
	#bottom wins if
	elif(checkBoard[6]!='*' and checkBoard[6]==checkBoard[7] and checkBoard[7]==checkBoard[8]):
		return True
	#left wins if
	elif(checkBoard[0]!='*' and checkBoard[0]==checkBoard[3] and checkBoard[3]==checkBoard[6]):
		return True
	#middle wins if
	elif(checkBoard[1]!='*' and checkBoard[1]==checkBoard[4] and checkBoard[4]==checkBoard[7]):
		return True
	#Right wins if
	elif(checkBoard[2]!='*' and checkBoard[2]==checkBoard[5] and checkBoard[5]==checkBoard[8]):
		return True
	#diagnol left wins
	elif(checkBoard[0]!='*' and checkBoard[0]==checkBoard[4] and checkBoard[4]==checkBoard[8]):
		return True
	#diagnol right wins
	elif(checkBoard[2]!='*' and checkBoard[2]==checkBoard[4] and checkBoard[4]==checkBoard[6]):
		return True
	else:
		return False

def userChoice():
	inputGood=0
	while (inputGood==0):
		#Make sure user input is an integer
		try:
			spotSelect = int(input('Where would you like to place your '+ userID +':'))
		except ValueError:
			print ("Only Integers accepted.  Please try again.")
		else:
			#make sure it is an integer on the board that has not already been selected
			for i in selectionList:
				if (int(spotSelect)==i):
					selectionList.remove(i)
					#update board to insert users X or O
					board.pop(i)
					board.insert(i, userID)
					inputGood=1
					return(board)
					
			print("Please try again that location is not available")

def easyComputerChoice():
	#dumb computer method randomly generate an unused location and print an X or O there
	lengthOfList = len(selectionList) - 1
	#generate random number of length list
	compSelect = random.randint(0,lengthOfList)
	compChoice=selectionList[compSelect]
	selectionList.remove(compChoice)
	#update board to insert users X or O
	board.pop(compChoice)
	board.insert(compChoice, computerID)
	print("\nThe Computer placed at location", compChoice)
	return(board)
					
def hardComputerChoice():
	#smart computer algorithim.  Check if comp can win, check if user can win and block, play a corner, play a middle, play a side.
	#try every location and see if any of them are a winner
	checkBoard=(list(board))
	for i in selectionList:
		checkBoard.pop(i)
		checkBoard.insert(i,computerID)
		if (checkWinner(checkBoard)==True):
			selectionList.remove(i)
			board.pop(i)
			board.insert(i,computerID)
			print("\nThe Computer placed at  location", i)
			return (board)
		else:
			checkBoard=(list(board))

	#try every location and make sure user cant win on next move
	for i in selectionList:
		checkBoard.pop(i)
		checkBoard.insert(i,userID)
		if (checkWinner(checkBoard)==True):
			selectionList.remove(i)
			board.pop(i)
			board.insert(i,computerID)
			print("\nThe Computer placed at location", i)
			return (board)
		else:
			checkBoard=(list(board))

	#Choose corner if available
	for i in selectionList:
		if (i==0 or i==2 or i==6 or i==8):
			selectionList.remove(i)
			board.pop(i)
			board.insert(i,computerID)
			print("\nThe Computer placed at  location", i)
			return (board)

	#Choose middle if available
	for i in selectionList:
		if (i==4):
			selectionList.remove(i)
			board.pop(i)
			board.insert(i,computerID)
			print("\nThe Computer placed at  location", i)
			return (board)

	#Choose sides if available
	for i in selectionList:
		if (i==1or i==3 or i==5 or i==7):
			selectionList.remove(i)
			board.pop(i)
			board.insert(i,computerID)
			print("\nThe Computer placed at  location", i)
			return (board)	


#set the board as an empty list
board=['*','*','*','*','*','*','*','*','*']
selectionList=[0,1,2,3,4,5,6,7,8,]
#user selects if they want ot be X or O and make the computer be opposite
userID=userMenuSelect()
if (userID=='X'):
	computerID='O'
else:
	computerID='X'
#get difficulty level from user
level = difficultyLevel()
#find out who gets the first move
if(firstMove()==0):
	whosTurn='comp'
else:
	whosTurn='user'
#keep this true untill we have a winner or tie
gameOn=True

while gameOn:
	if(whosTurn=='user'):
		userChoice()
		printBoard()
		#check if there is a winner
		if(checkWinner(board)==True):
			print("You win!")
			gameOn=False
		#check if there is a tie
		elif(not selectionList):
			print("It is a Tie")
			gameOn=False
		else:
			whosTurn='comp'
	else:
		#check difficulty level and play computer as hard or easy
		if (level==0):
			easyComputerChoice()
			printBoard()
		else:
			hardComputerChoice()
			printBoard()
		#check if there is a winner
		if(checkWinner(board)==True):
			print("Computer wins.")
			gameOn=False
		#check if there is a tie
		elif(not selectionList):
			print("It is a Tie")
			gameOn=False
		else:
			whosTurn='user'

print("Thanks for playing come back again soon.")