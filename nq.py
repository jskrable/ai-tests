# nq.py
# author: Jack Skrable
# date: 09/19/2018
# desc: solves the n-queens problem recursively 

import sys
import cProfile

def safe(board,col):
	# loop thru previous columns
	for i in range(col):
		# attacked if in the same row
		if (board[i]==board[col]):
			return False
		# attacked if on a diag
		if (col-i==abs(board[col]-board[i])):
			return False
	# safe otherwise
	return True

def solve(board,col,n):
	# end if past the last column
	if (col == n): 
		return True
	else:
		# loop thru rows
		for i in range(n):
			# place queen
			board[col]=i
			if safe(board,col):
				# if safe, try the next column
				solved=solve(board,col+1,n)
				# if we hit the end, all are safe
				if solved:
					return True
		return False

def display(board):
	# init row string
	row = ''
	# spacer row
	print()
	# loop thru columns
	for col in board:
		# loop thru rows
		for i in range(len(board)):
			if i == col:
				# place queen
				row += 'Q|' 
			else:
				# empty square
				row += '_|'
		# print row
		print(row)
		# empty row string for next loop
		row = ''
		
	# end spacer row
	print()

def main():

	# get n from cmd line arg
	n = int(sys.argv[1])

	# init board
	board = [-1]*n
	#solution = [[0]*n for i in range(n)]
	# solve for n
	solve(board,0,n)
	# print solution
	print(board)
	# display solution board
	display(board)

if __name__ == "__main__":
	# profile stats on run
	cProfile.run('main()')