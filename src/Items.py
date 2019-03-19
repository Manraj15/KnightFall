
'''The following class is repsoble for acting as a parent class to all other item types
    Last updated in March 17 2019
'''

class Item:
	img_path = None
	points = None
	# The x and y coordinated will be in pixels
	xCoord = None
	yCoord = None

	def __init__(self, img_path, points, xCoord, yCoord):
		self.img_path = img_path
		self.points = points
		self.xCoord = xCoord
		self.yCoord = yCoord

	def get_path(self):
		return self.img_path

	def get_points(self):
		return this.points

