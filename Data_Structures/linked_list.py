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
	as their data. Any arguments, if passed, will be appended to the list in the
	order they are passed. If they are lists, their elements will be appended one
	by one."""
	def __init__(self, *args):
		self.head = None
		self.length = 0
		for arg in args:
			if type(arg) is 'list':
				for element in args[0]:
					self.append(element)
			elif type(arg) is not 'NoneType':
				self.append(arg)

	def prepend(self, data):
		"""Prepends the list with the passed data"""
		self.insert(data, 0)

	def insert(self, data, index):
		"""Inserts the passed data (first parameter) at an index in the list
		specified by the second parameter. If the passed index is too high, throws
		an error."""
		if index > length:
			raise InputError
		new = ListNode(data)
		current = self.head
		for x in range(index - 1):
			current = current.next
		new.next = current.next
		current.next = new
		length += 1

	def append(self, data):
		"""Append the passed data to the LinkedList."""
		self.insert(data, self.length)

	def get(self, index):
		"""Returns the element at the passed index in the list."""
		current = self.head
		for x in range(length):
			current = current.next
		return current.data

	def remove_front(self):
		"""Removes the front element from the list."""
		delete(0)

	def delete(self, index):
		"""Delete whatever element is at the passed index in the LinkedList."""
		if index >= length:
			raise InputError
		if index is 0:
			self.head = self.head.next
		else:
			current = self.head
			for x in range(index - 2):
				current = current.next
			current.next = current.next.next
		length -= 1

	def remove_end(self):
		"""Removes the last element from the list."""
		delete(self.length)

	def __str__(self):
		to_print = "["
		current = self.head
		if current is not None:
			to_print.append(current)
			current = current.next
		while current is not None:
			to_print.append(", " + current)
			current = current.next
		to_print.append("]")
		print(to_print)
