# tictactoe.py
# author: Jack Skrable
# date: 10/03/2018
# desc: evaluates positions in a tictactoe game

import random

# function to randomly populate a complete board
def pop(board):

	# loop thru columns
	for i in range(len(board)):
		# random populate positions
		if random.randint(1,2) > 1:
			board[i] = 1
		else: 
			board[i] = 0
	return board

# function to display board
def display(board):

	# init display row
	show = ''
	# loop thru columns
	for i in range(len(board)):
		# show O is val is 0
		if board[i]== 0:
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

# function to evaluate board
def eval(board):
	# check all win positions for a complete row
	if ((board[7] == board[8] == board [9]) or
		(board[4] == board[5] == board [6]) or
		(board[1] == board[2] == board [3]) or 
		(board[1] == board[4] == board [7]) or 
		(board[2] == board[5] == board [8]) or
		(board[3] == board[6] == board [9]) or
		(board[7] == board[5] == board [3]) or 
		(board[1] == board[5] == board [9])):
		return 1
	# if none return draw
	else:
		return 0

def main():

	# create empty board
	board = [-1]*10
	# random full board
	pop(board)
	# display board
	display(board)
	#print(board)
	# print results of eval
	# 0 for draw 1 for win
	print(eval(board))

if __name__ == "__main__":
	main()