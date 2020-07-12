from RD_tool import App
from set_operation import SetOperation
import unittest

class SetTest(unittest.TestCase):

	"""Test case utilisé pour tester les fonctions du module 'random'."""

	def setUp(self):
		"""Initialisation des tests."""
		heroes = ['Thor', 'Captain America', 'Iron Man', 'Spiderman', 'Batman', 'Superman', 'Wonderwoman']
		marvel = ['Captain America', 'Iron Man', 'Spiderman', 'Thor', 'Black Widow']

		self.mySet = SetOperation(heroes, marvel)

	def test_intersection(self):
		self.mySet.get_intersection()
		self.assertEqual(self.mySet.intersection, {'Spiderman', 'Captain America', 'Iron Man', 'Thor'})

	def test_difference(self):
		self.mySet.get_difference()
		self.assertEqual(self.mySet.difference, {'Batman', 'Superman', 'Wonderwoman'})

	def test_difference(self):
		self.mySet.get_union()
		self.assertEqual(self.mySet.union, {'Thor', 'Captain America', 'Iron Man', 'Spiderman', 'Batman', 'Superman', 'Wonderwoman', 'Captain America', 'Iron Man', 'Spiderman', 'Thor', 'Black Widow'})


unittest.main()