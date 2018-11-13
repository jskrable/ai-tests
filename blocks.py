class Block:

	# init block state
	def __init__(self,id,on,table):
		self.id = id
		self.on = on
		table[id] = self
		for i in table:
			if table[i].on != 0:
				table[i].on.clear = False
		
		self.clear = True

	# try to move block
	def move(self,dest,test):

		# simpler if to table
		if dest == 'table':
			if self.clear:
				if not test:
					self.on = 0
				return True
		# otherwise check clear for both
		else:
			if self.clear and dest.clear:
				if not test:
					self.on = dest
					dest.clear = False
				return True
			else:
				return False

class Node():
	def __init__(self,node):
		
		self.a = Block(node['a'].id, lambda x: 0 if node['a'].on == 0 else eval(node['a'].on.id),node)
		self.b = Block(node['b'].id, lambda x: 0 if node['b'].on == 0 else eval(node['b'].on.id),node)
		self.c = Block(node['c'].id, lambda x: 0 if node['c'].on == 0 else eval(node['c'].on.id),node)

		self.node = dict(node)
		self.node['a'] = self.a
		self.node['b'] = self.b
		self.node['c'] = self.c
		self.goal = False
		self.subgoal = False
		self.moves = []

		if node['a'].on == node['b'] and node['b'].on == node['c'] and node['c'].on == 'table':
			self.goal = True

		if node['a'].on == node['b'] or node['b'].on == node['c'] or node['c'].on == 'table':
			self.subgoal = True

		for i in node:
			self.moves.append((node[i],'table'))

			for j in node:
				if i != j:
					if node[i].move(node[j],True):
						self.moves.append((node[i],node[j]))


def moves(node):
	moves = []
	for i in node:
		moves.append((i,'table'))

		for j in node:
			if i != j:
				if node[i].move(node[j],True):
					moves.append((i,j))
	return moves

def search(node,depth):
	if node.goal:
		return True
	if depth > 8:
		print('Depth max exceeded')
		return False
	for i,j in node.moves:
		child_node = Node(node.node)
		i.move(j,False)
		if search(child_node,depth+1):
			print('Puzzle complete')
			break

board = {}
a = Block('a',0,board)
b = Block('b',0,board)
c = Block('c',a,board)
start = Node(board)
search(start,0)



