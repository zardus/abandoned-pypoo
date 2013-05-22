class Analysis:
	''' The analysis glue. '''
	def __init__(self, parser):
		self.parser = parser

	def update(self):
		''' Updates the analysis with new program events. '''

		for e in self.parser.get_new_events():
			pass # TODO
