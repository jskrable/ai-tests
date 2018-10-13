# tictactoe.py
# author: Jack Skrable
# date: 10/03/2018
# desc: evaluates positions in a tictactoe game

import random
from math import inf

# list of win scenarios
win_conditions = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),
	(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

"""
# function to randomly populate a complete board
def pop(board,full):

	# populate board completely
	if full:
		for i in range(len(board)):
			if random.randint(1,2) > 1:
				board[i] = 1
			else: 
				board[i] = 0
		return board
	# populate a partial board
	else:
		for i in range(random.randint(1,len(board))):
mini			if i%2 == 0:
				board[i] = 1
			else: 
				board[i] = 0
		return board
"""

def run(board,first):
	while not end(board):
		if win(board) != 0:
			print("WINNER ", + str(win(board)))
			
		bestMove(board,first)
	return board

# minimax function
def minimax(board,depth,player):

	nodes = 0

	if player == -1:
		best = +inf
	else:
		best = -inf

	if end(board):
		return win(board)

	for i in range(1,len(board)):
		if board[i] == 0:
			board[i] = player
			best = max(minimax(board,depth+1,-player))
			board[i] = 0
		"""
		value = minimax(board,depth+1,-player)
		best = max(best,value)
		"""
	return best

def bestMove(board,player):
	best_value = -inf
	best_move = -1

	for i in range(1,len(board)):
		if board[i] == 0:
			board[i] = player
			move_value = minimax(board,0,player)
			board[i] = 0

			if move_value > best_value:
				best_move = i
				best_value = move_value

	print("The value of the best move is: " + str(best_move))
	return best_move


# dumb recursive function to play a random open square
def playRand(board,player):

	# try a random square
	square = random.randint(1,len(board))
	# if not empty, try again
	if board[square] != 0:
		play(board,player)
	else:
		board[square] = player


# function to display board
def display(board):

	# init display row
	show = ''
	# loop thru columns
	for i in range(len(board)):
		# show O is val is 0
		if board[i]== -1:
			show += 'O'
		# show X if val is 1
		elif board[i] == 1:
			show += 'X'
		# otherwise show blank
		else:
			show += ' '
	
	# print board
	print()	
	print(show[1:4])
	print(show[4:7])
	print(show[7:10])
	print()

# function to end game and clear board
def reset():
	board = [0]*10
	return board

# function to determine win state
def win(board):
	win = 0
	for x,y,z in win_conditions:
		if board[x]==board[y]==board[z]!=0:
			win = board[x]
	return win

def draw(board):
	empty = False
	for i in range(1,len(board)):
			if board[i] == 0:
				empty = True
	return not empty

def end(board):
	return win(board) != 0 or draw(board)
				

# function to evaluate board
def state(board):
	# list of win scenarios
	win_conditions = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),
		(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
	# init vars
	win = 0
	adv = 0
	# loop thru win conditions
	for x,y,z in win_conditions:
		# if three in a row win
		if board[x]==board[y]==board[z]!=0:
			win = board[x]
			# assign adv to winner
			adv = board[x]
		# give adv to player w one move to win
		elif (board[x]==board[y]==-1 and board[z]==0) or (board[x]==board[z]==-1 and board[y]==0) or (board[y]==board[z]==-1 and board[x]==0):
			adv = -1
		elif (board[x]==board[y]==1 and board[z]==0) or (board[x]==board[z]==1 and board[y]==0) or (board[y]==board[z]==1 and board[x]==0):
			adv = 1
		# else give to player who went first	
		else:
			adv = 1

	return win, adv

def main():

	# create empty board
	board = [-1]*10
	# random partial board
	#pop(board,False)
	# display board
	display(board)
	#print(board)
	# print results of eval
	# 0 for draw 1 for win
	#print(eval(board))

if __name__ == "__main__":
	main()