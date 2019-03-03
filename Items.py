
#The following class should be used as a parent for specifc items
#Before anyone adds to this class, please talk to me (Manraj)

class Item:
	img_path = None
	points = None
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

