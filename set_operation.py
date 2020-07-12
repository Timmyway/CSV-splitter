class SetOperation(object):
	"""docstring for SetOperation"""
	def __init__(self, original, dedup):
		super(SetOperation, self).__init__()
		self.original = set(original)
		self.dedup = set(dedup)

	def get_difference(self):
		''' Original - dedup '''
		self.difference = self.original - self.dedup		

	def get_intersection(self):
		''' Original - dedup '''
		self.intersection = self.original.intersection(self.dedup)

	def get_intersection(self):
		''' Original - dedup '''
		self.intersection = self.original.intersection(self.dedup)

	def get_union(self):
		''' Original - dedup '''
		self.union = self.original.union(self.dedup)
		

if __name__ == '__main__':
	heroes = ['Thor', 'Captain America', 'Iron Man', 'Spiderman', 'Batman', 'Superman', 'Wonderwoman']
	marvel = ['Captain America', 'Iron Man', 'Spiderman', 'Thor', 'Black Widow']

	s = SetOperation(heroes, marvel)
	s.get_difference()
	s.get_intersection()
	print(f'Heroes that are not Marvel member: {s.difference}')
	print(f'Marvel heroes: {s.intersection}')
	