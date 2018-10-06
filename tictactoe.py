# tictactoe.py
# author: Jack Skrable
# date: 10/03/2018
# desc: evaluates positions in a tictactoe game

import random

# function to randomly populate a complete board
def pop(board):

	for col in range(len(board)):
		for row in range(len(board)):
			if random.randint(1,2) > 1:
				board[col][row] = 'X'
			else: 
				board[col][row] = 'O'
	return board

# function to evaluate a complete board
def eval(board):
	

def main():

	# create empty board
	board = [['e']*3 for i in range(3)]
	# random full board
	pop(board)
if __name__ == "__main__":
	main()