# tictactoe.py
# author: Jack Skrable
# date: 10/03/2018
# desc: evaluates positions in a tictactoe game

import random

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
			if i%2 == 0:
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
	# list of win scenarios
	win_conditions = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),
		(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
	# init win
	win = 0
	# loop thru win conditions
	for x,y,z in win_conditions:
		# if three in a row win
		if board[x]==board[y]==board[z]!=-1:
			win = 1

	return win

def main():

	# create empty board
	board = [-1]*10
	# random partial board
	pop(board,False)
	# display board
	display(board)
	#print(board)
	# print results of eval
	# 0 for draw 1 for win
	print(eval(board))

if __name__ == "__main__":
	main()