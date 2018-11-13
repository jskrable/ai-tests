n = 3

table = [[]]*n

# start position of blocks
start = [['B'],['C','A'],[]]

def clearTop

# check for win conditions
def goal(table):
	# winning stack
	stack = ['A','B','C']
	# loop thru table check for win
	for i in range(len(table)):
		if table[i] == stack:
			return True
	# return false if no win stack
	return False

def precond(table,block,dest):
	if table[src] 

# perform move of block
def move(table,src,dest):
	# insert to new dest stack
	table[dest].insert(0,table[src][0])
	# drop from src stack
	del table[src][0]
	return table

class Block:

	def __init__(self,id,on):
		self.id = id
		self.on = on


	def clear(self):
		for i in node:
			if node[i].on != 'table':
				node[i].on.clear = False
		
		self.clear = True

	def move(self,dest):

		if dest == 'table':
			self.clear()
			if self.clear:
				self.on = 'table'
		else:
			self.clear()
			dest.clear()
			if self.clear and dest.clear:
				self.on = dest
				dest.clear = False
				return True
			else:
				return False



class State:

	def __init__(self,a,b,c):
		self.goal = False
		self.subgoal = False

		if a.on == b and b.on == c and c.on == 'table':
			self.goal = True
		elif a.on == b or b.on == c or c.on == 'table':
			self.subgoal = True
		

class Node:

	def __init__(self,depth,state):
		self.depth = depth



class Stack:

	def __init__(self,)