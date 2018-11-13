n = 3

table = [[]]*n

# start position of blocks
start = [[3],[1,2],[]]

# check for win conditions
def goal(table):
	# get winning stack
	stack = []
	for i in range(len(table)):
		stack.append(i+1)
	# loop thru table check for win
	for i in range(len(table)):
		if table[i] == stack:
			return True
	# return false if no win stack
	return False

# perform move of block
def move(table,src,dest):
	# insert to new dest stack
	table[dest].insert(0,table[src][0])
	# drop from src stack
	del table[src][0]
	return table

