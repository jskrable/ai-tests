table = [[],[],[]]

goal = [[1],[2],[3]]

start = [[3],[1,2],[]]

def move(table,src,dest):
	table[dest].insert(0,table[src][0])
	del table[src][0]