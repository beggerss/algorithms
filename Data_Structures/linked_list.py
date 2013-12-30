#!/usr/bin/python
# Author: Ben Eggers

# Implementation of a linked list in Python.

class ListNode:
	"""ListNode class to be used in the LinkedList."""
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	"""LinkedList class. Note that nodes in the list can have different datatypes
	as their data."""
	def __init__(self):
		self.head = None
		self.length = 0

	def append(self, data):
		new = ListNode(data)
		current = self.head
		for x in range(length):
			current = current.next
		# current is now pointing at the end of the list
		current.next = new
		return self

	