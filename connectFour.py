#!/usr/bin/python

import random
#To copy a 2D array or matrix need to import copy
import copy

#Nicholas Cipriano 
#Connect 4 Game written in Python

def printInstructions():
	#Print Help instructions to make it clear where the R or Y will be placed
	print("Welcome to Nicks game of Connect Four.  Select weather you would like to play as Red or Yellow.  Computer will randomly pick who will go first.  When it is your turn You will enter a number from 0 to 6 to call out what column you would like to drop into.  0 will be the far left 6 the far right.")

def userMenuSelect():
	#untill a X or a Y is selected keep trying to recieve correct input from user
	userHasSelected=0
	userID = '*'

	while (userHasSelected==0):
		menuInput = input('Would you like to play as R or Y?  type help for instructions: ')
		if(menuInput.lower()=='help'):
			printInstructions()
		elif(menuInput.lower()=='r'):
			userID='R'
			return userID
		elif(menuInput.lower()=='y'):
			userID='Y'
			return userID
		else:
			print("The only acceptable inputs are R, Y, and Help.  please try again")

def firstMove():
	#Randomly generate a 0 or 1 to decide who will get the first move
	if (random.randint(0,1)==0):
		print("Computer gets first move")
		return 0
	else:
		print("You get first move")
		return 1

def printBoard():
	#print connect 4 board.  gameBoard[][] is a nested list of the 6x7 board matrix
	#print a linebreak before printing board to clean it up
	print('\n')
	for i in gameBoard:
		print (i)


def checkWinner(checkBoard):
	#Check 4 in a row if horizontal sideways or diagnol anywhere on board
	row = 0
	column = 0
	#for loop through the rows
	for i in checkBoard:
		#for loop through the columns
		for x in checkBoard[row]:
			if(x=='R' or x=='Y'):
				#check if there is a horizontal 4 in a row
				if(column>2 and checkBoard[row][column]==checkBoard[row][column-1] and checkBoard[row][column]==checkBoard[row][column-2] and checkBoard[row][column]==checkBoard[row][column-3]):
					#print("that is four in a horizontal row at row", row, "and column", column)
					return True
				#Check if there is a verticle 4 in a row
				elif(row>2 and checkBoard[row][column]==checkBoard[row-1][column] and checkBoard[row][column]==checkBoard[row-2][column] and checkBoard[row][column]==checkBoard[row-3][column]):
					#print("that is four in a verticle row at column", column, "row", row)
					return True

				#check if there is a right diagnol 4 in a row
				elif(column>2 and row<3 and checkBoard[row][column]==checkBoard[row+1][column-1] and checkBoard[row][column]==checkBoard[row+2][column-2] and checkBoard[row][column]==checkBoard[row+3][column-3]):
					#print("that is four in a diagnol right row my friend")
					return True

					#check if there is a left diagnol 4 in a row
				elif(column<4 and row<3 and checkBoard[row][column]==checkBoard[row+1][column+1] and checkBoard[row][column]==checkBoard[row+2][column+2] and checkBoard[row][column]==checkBoard[row+3][column+3]):
					#print("that is four in a diagnol left row my friend")
					return True

			#move column to the right 1
			column=column+1
		#move row down 1
		row=row+1
		#reset column back to 0 on new row
		column = 0
	#if no winner found return false
	return False

def checkHorizontalState(testID):
	#check if the disk can be used to help create a horizontal of 4 if so place disk 
	add=1
	for i in range(0,7):
		#Run through every location with a disk in it
		while ((columnStack[i]+add)<=5):
			#check if you can create 4 in a row horizontal to the left if you can, drop it to the left side
			if(i > 2 and gameBoard[columnStack[i]+add][i]==testID and (gameBoard[columnStack[i]+add][i-1]==testID or gameBoard[columnStack[i]+add][i-1]=='*') and (gameBoard[columnStack[i]+add][i-2]==testID or gameBoard[columnStack[i]+add][i-2]=='*')and (gameBoard[columnStack[i]+add][i-3]==testID or gameBoard[columnStack[i]+add][i-3]=='*')):
				#check if you can drop a disk to the left side or if it will fall to far
				#if we are on the bottom row do the following, check that spot to the left is empty if it is place disk there
				if(columnStack[i]+add==5 and gameBoard[columnStack[i]+add][i-1]=='*'):
					gameBoard[columnStack[i]+add].pop(i-1)
					gameBoard[columnStack[i]+add].insert(i-1,computerID)
					columnStack[i-1]=columnStack[i-1]-1
					print("computer places disk in row", i-1)
					return(gameBoard)
				#If spot to the left is full with the same disk type check the spot to the left 2 down if that is empty place computerID there
				elif(columnStack[i]+add==5 and gameBoard[columnStack[i]+add][i-1]==testID and gameBoard[columnStack[i]+add][i-2]=='*'):
					gameBoard[columnStack[i]+add].pop(i-2)
					gameBoard[columnStack[i]+add].insert(i-2,computerID)
					columnStack[i-2]=columnStack[i-2]-1
					print("computer places disk in row", i-2)
					return(gameBoard)
				#if spot is not on bottom row make sure an item can be placed next to it and that the location is empty
				elif (columnStack[i]+add!=5 and gameBoard[columnStack[i]+add+1][i-1]!='*' and gameBoard[columnStack[i]+add][i-1]=='*'):
					gameBoard[columnStack[i]+add].pop(i-1)
					gameBoard[columnStack[i]+add].insert(i-1,computerID)
					columnStack[i-1]=columnStack[i-1]-1
					print("computer places disk in row", i-1)
					return(gameBoard)
				#if spot to the left is full with the same disk type and it is not on bottom row make sure an item can be placed 2 down to the left and find that the location is empty
				elif (columnStack[i]+add!=5 and gameBoard[columnStack[i]+add][i-1]==testID and gameBoard[columnStack[i]+add+1][i-2]!='*'and gameBoard[columnStack[i]+add][i-2]=='*'):
					gameBoard[columnStack[i]+add].pop(i-2)
					gameBoard[columnStack[i]+add].insert(i-2,computerID)
					columnStack[i-2]=columnStack[i-2]-1
					print("computer places disk in row", i-2)
					return(gameBoard)
			#check if you can create 4 in a row horizontal to the right if you can, drop it to the right side
			if(i< 4 and gameBoard[columnStack[i]+add][i]==testID and (gameBoard[columnStack[i]+add][i+1]==testID or gameBoard[columnStack[i]+add][i+1]=='*') and (gameBoard[columnStack[i]+add][i+2]==testID or gameBoard[columnStack[i]+add][i+2]=='*')and (gameBoard[columnStack[i]+add][i+3]==testID or gameBoard[columnStack[i]+add][i+3]=='*')):
				#check if you can drop a disk to the right side or if it will fall to far
				#if we are on the bottom row do the following, check that spot to the right is empty if it is place computerID there
				if(columnStack[i]+add==5 and gameBoard[columnStack[i]+add][i+1]=='*'):
					gameBoard[columnStack[i]+add].pop(i+1)
					gameBoard[columnStack[i]+add].insert(i+1,computerID)
					columnStack[i+1]=columnStack[i+1]-1
					print("computer places disk in row", i+1)
					return(gameBoard)
				#If spot to the right is full with disk of same type check the spot to the right 2 down if that is empty place computerID there
				elif(columnStack[i]+add==5 and gameBoard[columnStack[i]+add][i+1]==testID and gameBoard[columnStack[i]+add][i+2]=='*'):
					gameBoard[columnStack[i]+add].pop(i+2)
					gameBoard[columnStack[i]+add].insert(i+2,computerID)
					columnStack[i+2]=columnStack[i+2]-1
					print("computer places disk in row", i+1)
					return(gameBoard)
				#if spot is not on bottom row make sure an item can be placed next to it and that the location is empty
				elif (columnStack[i]+add!=5 and gameBoard[columnStack[i]+add+1][i+1]!='*' and gameBoard[columnStack[i]+add][i+1]=='*'):
					gameBoard[columnStack[i]+add].pop(i+1)
					gameBoard[columnStack[i]+add].insert(i+1,computerID)
					columnStack[i+1]=columnStack[i+1]-1
					print("computer places disk in row", i+1)
					return(gameBoard)
				#if spot to the right is full with disk of same type and it is not on bottom row make sure an item can be placed 2 down to the right and find that the location is empty
				elif (columnStack[i]+add!=5 and gameBoard[columnStack[i]+add][i+1]==testID and gameBoard[columnStack[i]+add+1][i+2]!='*' and gameBoard[columnStack[i]+add][i+2]=='*'):
					gameBoard[columnStack[i]+add].pop(i+2)
					gameBoard[columnStack[i]+add].insert(i+2,computerID)
					columnStack[i+2]=columnStack[i+2]-1
					print("computer places disk in row", i+2)
					return(gameBoard)

			add=add+1
		add=1

def checkDiagnolState(testID):
	add=1
	for i in range(0,7):
		#Run through every location with a disk in it
		while ((columnStack[i]+add)<3):
			#check if you can create 4 in a row diagnol to the left if you can, drop it to the left side
			if(i > 2 and gameBoard[columnStack[i]+add][i]==testID and (gameBoard[columnStack[i]+add+1][i-1]==testID or gameBoard[columnStack[i]+add+1][i-1]=='*') and (gameBoard[columnStack[i]+add+2][i-2]==testID or gameBoard[columnStack[i]+add+2][i-2]=='*')and (gameBoard[columnStack[i]+add+3][i-3]==testID or gameBoard[columnStack[i]+add+3][i-3]=='*')):
				#check if you can drop a disk to the left side or if it will fall to far
				#make sure an item can be placed next to it and that the location is empty
				if (gameBoard[columnStack[i]+add+2][i-1]!='*' and gameBoard[columnStack[i]+add+1][i-1]=='*'):
					gameBoard[columnStack[i]+add+1].pop(i-1)
					gameBoard[columnStack[i]+add+1].insert(i-1,computerID)
					columnStack[i-1]=columnStack[i-1]-1
					print("computer places disk in row", i-1)
					return(gameBoard)
				#if spot to the left is full with the same color disk make sure an item can be placed 2 down to the left and find that the location is empty
				elif (gameBoard[columnStack[i]+add+1][i-1]==testID and gameBoard[columnStack[i]+add+3][i-2]!='*' and gameBoard[columnStack[i]+add+2][i-2]=='*'):
					gameBoard[columnStack[i]+add+2].pop(i-2)
					gameBoard[columnStack[i]+add+2].insert(i-2,computerID)
					columnStack[i-2]=columnStack[i-2]-1
					print("computer places disk in row", i-2)
					return(gameBoard)
			#check if you can create 4 in a row diagnol to the right if you can, drop it to the right side
			if(i < 4 and gameBoard[columnStack[i]+add][i]==testID and (gameBoard[columnStack[i]+add+1][i+1]==testID or gameBoard[columnStack[i]+add+1][i+1]=='*') and (gameBoard[columnStack[i]+add+2][i+2]==testID or gameBoard[columnStack[i]+add+2][i+2]=='*')and (gameBoard[columnStack[i]+add+3][i+3]==testID or gameBoard[columnStack[i]+add+3][i+3]=='*')):
				#check if you can drop a disk to the right side or if it will fall to far
				#make sure an item can be placed next to it and that the location is empty
				if (gameBoard[columnStack[i]+add+2][i+1]!='*' and gameBoard[columnStack[i]+add+1][i+1]=='*'):
					gameBoard[columnStack[i]+add+1].pop(i+1)
					gameBoard[columnStack[i]+add+1].insert(i+1,computerID)
					columnStack[i+1]=columnStack[i+1]-1
					print("computer places disk in row", i+1)
					return(gameBoard)
				#if spot to the right is full with the same color disk make sure an item can be placed 2 down to the right and find that the location is empty
				elif (gameBoard[columnStack[i]+add+1][i+1]==testID and gameBoard[columnStack[i]+add+2][i+1]!='*'and gameBoard[columnStack[i]+add+2][i+2]=='*'):
					#print("Place the disk here at row",columnStack[i]+add, "column", i+2,)
					gameBoard[columnStack[i]+add+2].pop(i+2)
					gameBoard[columnStack[i]+add+2].insert(i+2,computerID)
					columnStack[i+2]=columnStack[i+2]-1
					print("computer places disk in row", i+2)
					return(gameBoard)

			add=add+1
		add=1

def userChoice():
	inputGood=0
	while (inputGood==0):
		#Make sure user input is an integer
		try:
			spotSelect = int(input('In what column would you like to place youdr disk(must be number between 0 and 6):'))
		except ValueError:
			print ("Only Integers accepted.  Please try again.")
		else:
			userColumnSelect = int(spotSelect)
			#make sure it is one of the columns available 
			if(userColumnSelect>=0 and userColumnSelect<=6):
				if(columnStack[userColumnSelect]>=0):

					#update game board with where user dropped the Disk
					gameBoard[columnStack[userColumnSelect]].pop(userColumnSelect)
					gameBoard[columnStack[userColumnSelect]].insert(userColumnSelect,userID)

					#update column stack to say a disk has been placed in that column
					columnStack[userColumnSelect]=columnStack[userColumnSelect]-1
					return(gameBoard)
			print("Please try again that location is not available")



def computerChoice():
	#since gameBoard is a matrix need to use deepcopy, just the list tag does not create new matrix
	testBoard = copy.deepcopy(gameBoard)

	#See if the computer can win in the next move if so place disk to win the game
	for col in range(0,7):
		if (columnStack[col]>-1):
			testBoard[columnStack[col]].pop(col)
			testBoard[columnStack[col]].insert(col,computerID)

		if(checkWinner(testBoard)==True):
			gameBoard[columnStack[col]].pop(col)
			gameBoard[columnStack[col]].insert(col,computerID)
			columnStack[col]=columnStack[col]-1
			print("computer goes for win and places disk in row", col)
			return(gameBoard)
		else:
			testBoard = copy.deepcopy(gameBoard)

	#See if the user can win next move if so block him so he cant win
	for col in range(0,7):
		if (columnStack[col]>-1):
			testBoard[columnStack[col]].pop(col)
			testBoard[columnStack[col]].insert(col,userID)

		if(checkWinner(testBoard)==True):
			gameBoard[columnStack[col]].pop(col)
			gameBoard[columnStack[col]].insert(col,computerID)
			columnStack[col]=columnStack[col]-1
			print("computer places disk in row", col)
			return(gameBoard)
		else:
			testBoard = copy.deepcopy(gameBoard)

	#Play bottom center first, known if you play bottom center first the worst you can do is tie
	if(gameBoard[5][3]=='*'):
		gameBoard[columnStack[3]].pop(3)
		gameBoard[columnStack[3]].insert(3,computerID)
		columnStack[3]=columnStack[3]-1
		print("computer places first disk in row 3")
		return(gameBoard)

	#Play Defense first block a diagnol of player diskss
	if (checkDiagnolState(userID)!=None):
		return(gameBoard)

	#Play Defense first block a horizontal row of player disks
	if (checkHorizontalState(userID)!=None):
		return(gameBoard)

	#Place on top of same color disk to try and go for verticle row
	for col in range(0,7):
		if(columnStack[col]<5 and columnStack[col]>-1 and gameBoard[columnStack[col]+1][col]==computerID):	
			gameBoard[columnStack[col]].pop(col)
			gameBoard[columnStack[col]].insert(col,computerID)
			columnStack[col]=columnStack[col]-1
			print("computer places disk in row", col)
			return(gameBoard)
	
	#Check if horizontal 4 is still possible and place on the side of disk to the right or the left to make horizontal row
	if (checkHorizontalState(computerID)!=None):
		return(gameBoard)
	
	#Check if diagnol 4 is still possible and place on the side of the diag disk to make diagnol row
	if(checkDiagnolState(computerID)!=None):
		return(gameBoard)
	
	#if none of the above have hope randomly place disk.  If it gets here most likely a tie
	randomGood=0
	randomNum=0
	while (randomGood==0):
		randomNum = random.randint(0,6)
		if (columnStack[randomNum]>-1):
			gameBoard[columnStack[randomNum]].pop(randomNum)
			gameBoard[columnStack[randomNum]].insert(randomNum,computerID)
			columnStack[randomNum]=columnStack[randomNum]-1
			print("computer places disk in row", randomNum)
			return(gameBoard)

#create game board matrix
gameBoard = [
['*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*'],
['*','*','*','*','*','*','*'],
]

columnStack=[5,5,5,5,5,5,5]
tieStack=[-1,-1,-1,-1,-1,-1,-1]

#user selects if they want ot be X or O and make the computer be opposite
userID=userMenuSelect()
if (userID=='R'):
	computerID='Y'
else:
	computerID='R'
#find out who gets the first move
if(firstMove()==0):
	whosTurn='comp'
else:
	whosTurn='user'

#Start the Game
gameOn=True

while gameOn:
	if(whosTurn=='user'):
		userChoice()
		printBoard()
		#check if there is a winner
		if(checkWinner(gameBoard)==True):
			print("You win!")
			gameOn=False
		#check if there is a tie
		elif(columnStack==tieStack):
			print("It is a Tie")
			gameOn=False
		#Move on to computers Turn
		else:
			whosTurn='comp'
	else:
		computerChoice()
		printBoard()
		#check if there is a winner
		if(checkWinner(gameBoard)==True):
			print("Computer wins.")
			gameOn=False
		#check if there is a tie
		elif(columnStack==tieStack):
			print("It is a Tie")
			gameOn=False
		else:
			whosTurn='user'

print("Thanks for playing come back again soon.")