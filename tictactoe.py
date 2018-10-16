# tictactoe.py
# author: Jack Skrable
# date: 10/03/2018
# desc: evaluates positions in a tictactoe game

import random
from math import inf

# list of win scenarios
win_conditions = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),
	(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

# function to run full game
def run(board,player):
	# print winner on win
	if win(board) != 0:
		print("WINNER")
	# print draw on draw
	elif draw(board):
		print("DRAW")
	# if not over keep playing
	while not end(board):
		# play best move
		board[bestMove(board,player)]=player
		# show board
		display(board)
		# recurse until end
		run(board,-player)
	# reset board
	board = reset()

# minimax function
def minimax(board,depth,player):

	# init leaf counter
	#nodes = 0

	# catch terminal states
	if end(board):
		# return scores for end
		# 10 for X win
		# -10 for O win
		# 0 for draw
		return win(board)*10
	# set endpoint bests by player
	elif player == 1:
		best_score = -inf
	else:
		best_score = +inf

	# run through squares
	for i in range(1,len(board)):
		# check if empty
		if board[i] == 0:
			# try to play
			board[i] = player
			# get best possible value of play using recursion
			# ALTER THIS TO TAKE DEPTH INTO ACCOUNT
			# value = value - depth??
			value = minimax(board,depth+1,-player) - (player*depth)
			# set best score by player
			if player == 1:
				best_score = max(best_score,value)
			else:
				best_score = min(best_score,value)
			# take back play
			board[i] = 0
	# return best score possible
	return best_score

# function that returns best move by player
def bestMove(board,player):

	"""
	if player == 1:
		# init vars
		best_value = -inf

		# loop through squares
		for i in range(1,len(board)):
			# if empty
			if board[i] == 0:
				# make move
				board[i] = player
				# get best possible value of move
				move_value = minimax(board,0,-1)
				# take move back
				board[i] = 0

				# set best move
				if move_value > best_value:
					best_move = i
					best_value = move_value
	else:
		best_value = +inf
		# loop through squares
		for i in range(1,len(board)):

			# if empty
			if board[i] == 0:
				# make move
				board[i] = player
				# get best possible value of move
				move_value = minimax(board,0,1)
				# take move back
				board[i] = 0

				# set best move
				if move_value < best_value:
					best_move = i
					best_value = move_value
	"""
	# set endpoint values
	if player == 1:
		best_value = -inf
	else:
		best_value = +inf

	# loop through squares
	for i in range(1,len(board)):
		# if empty
		if board[i] == 0:
			# make move
			board[i] = player
			# get best possible value of move
			move_value = minimax(board,0,-player)
			# take move back
			board[i] = 0

			# set best move
			if (player == 1 and move_value > best_value) or (player == -1 and move_value < best_value):
				best_move = i
				best_value = move_value

	# display value of best move
	print("The value of the best move is: " + str(best_value))
	print("The index of the best move is: " + str(best_move))
	return best_move

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
	# init win var
	win = 0
	# loop thru possible wins
	for x,y,z in win_conditions:
		if board[x]==board[y]==board[z]!=0:
			# set win to winning player
			win = board[x]
			break
	return win

# function to check for a push
def draw(board):
	# init empty var
	empty = False
	# loop thru squares
	for i in range(1,len(board)):
			if board[i] == 0:
				# update var if any are empty
				empty = True
				break
	# return true for no empty squares
	return not empty

# function to check for terminal state
def end(board):
	# check if win or draw
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
			break
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
	board = [0]*10

	# run game X goes first
	run(board,1)

if __name__ == "__main__":
	main()