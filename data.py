''' Datastructures used by the analyzer. '''

from collections import namedtuple

def Block():
	return namedtuple("Block", ['num_instructions', 'length', 'address', 'operations', 'dependencies' ])

def Event():
	return namedtuple("Event", ['event_type', 'address', 'length', 'value', 'block', 'taint'])

#import instructions
#
#class Block:
#	''' This class holds the information on a single extended basic block. The idea is to capture several pieces of data:
#
#		- the input information for a basic block (reads from memory and registers)
#		- the output information for a basic block (writes to memory and registers)
#		- what else?
#	'''
#
#	def __init__(self, start_addr, num_instructions):
#		self.num_instructions = [ ]
#		self.start_addr = [ ]
#		self.memory_ops = [ ]
#
#	def add_write(self, inst_addr, write_target, write_length, write_data = None):
#		#inst = program.get_instruction(inst_addr)
#		op = Write(write_target, write_length, write_data)
#		self.memory_ops.append(op)
#
#	def add_read(self, inst_addr, read_target, read_length, read_data = None):
#		#inst = program.get_instruction(inst_addr)
#		op = Read(read_target, read_length, read_data)
#		self.memory_ops.append(op)

#class MemOp:
#	''' This is a base class for memory operations. '''
#
#	def __init__(self, target, length, data):
#		self.target = target
#		self.length = length
#		self.data = data
#		self.dependencies = [ ]
#
#class Write(MemOp):
#	''' This is a class for describing memory writes. '''
#
#class Read(MemOp):
#	''' This is a class for describing memory writes. '''
