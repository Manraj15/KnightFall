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
		print(self.board)
