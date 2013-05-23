import data
from collections import defaultdict

class Analysis:
	''' The analysis glue. '''
	def __init__(self, parser):
		self.parser = parser
		self.last_block = None

		# various structures and indexes
		self.blockstarts = defaultdict(list)
		self.blocks = { }
		self.memory_writes = { } #TODO: ranges

	def update(self):
		''' Updates the analysis with new program events. '''

		for e in self.parser.get_new_events():
			if e.event_type == "block_entry":
				self.last_block = data.Block(e.address, e.length)
				self.blockstarts[e.address].append(last_block)
				self.blocks[(e.address, e.length)].append(last_block)
			if e.event_type == "memory_read":
				e.block = self.last_block
				self.last_block.operations.append(e)
			if e.event_type == "memory_write":
				e.block = self.last_block
				self.last_block.operations.append(e)
				self.memory_writes[e.address] = e
			if e.event_type == "conditional":
				# TODO, would require register taint tracking
				pass
