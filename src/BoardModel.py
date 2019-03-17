'''
The following class is used to simulate the current state of game
Las Updated March 17, 2019
'''

from random import randint

class BoardModel:
	board = []
	num_points = 0
	num_possible_moves = 0

	def init(self):
		self.makeBoard()

	#Generate the Board using numbers randomly 
	#generated from 1 to 4, each representing an item
	def make_board(self):
		inner_row = []
		for i in range(0, 6):
			for j in range(0, 6):
				inner_row.append(randint(1,4))
			self.board.append(inner_row)
		
    def update_num_points(self, num):
    	self.num_points = self.num_points + num

    def get_num(self):
    	return self.num_points

    def get_board(self):
		return self.board

	#For debugging purposes
	def print_board(self):

    def get_match(self, x, y):
        '''
        X=0 is the leftmost column
        Y=0 is the rightmost row
        Returns two variables containing the coordinates of the
        first set of matching numbers in a line: x1, y1, x2, y2
        if no match is foun, returns -1 -1 -1 -1
        '''
        #Note : this doesnt check out of bound indices yet
        
        #Check matches when x, y are in the center of the line of len 3
        if self.board[y][x] == self.board[y-1][x] and self.board[y][x] == self.board[y+1][x]:
            return x, y-1, x, y+1
        elif self.board[y][x] == self.board[y][x-1] and self.board[y][x] == self.board[y][x+1]:
            return x-1, y, x+1, y
        elif self.board[y][x] == self.board[y-1][x-1] and self.board[y][x] == self.board[y+1][x+1]:
            return x-1, y-1, x+1, y+1
        elif self.board[y][x] == self.board[y+1][x-1] and self.board[y][x] == self.board[y-1][x+1]:
            return x-1, y+1, x+1, y-1

        #Check matches when x, y are at the edges of a line of len 3
        for (i=x-1, i<=x+1; i++):
            for (j=y-1; j<=y+1; j++):
                if i!=x and j!=y and self.board[y][x] == self.board[j][i]:
                    retX1 = i
                    retY1 = j

                    if i<x:
                        retX2=i-1
                    elif i=x:
                        retX2=i
                    else:
                        retX2=i+1

                    if j<y:
                        retY2=j-1
                    elif j=y:
                        retY2=j
                    else:
                        retY2=j+1

                    if self.board[y][x] == self.board[retY2][retX2]:
                        return retX1, retY1, retX2, retY2
        return -1, -1, -1, -1
