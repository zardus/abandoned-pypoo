''' A reader for lackey output. '''

class Parser:
	def __init__(self, pipename):
		''' Opens the pipe, starts reading. '''
		self.pipe = open(pipename)

	def read(self):
		''' Reads events from Lackey, returning new basic blocks. '''

		# TODO: don't block
		while self.pipe.readline().strip():
