class SetOperation(object):
	"""docstring for SetOperation"""
	def __init__(self, original, dedup):
		super(SetOperation, self).__init__()
		self.original = original
		self.dedup = dedup

	def get_difference(self):
		''' Original - dedup '''
		self.original_minus_dedup = self.original - self.dedup
		return self.original_minus_dedup
		

if __name__ == '__main__':
	original = {'A', 'B', 'C', 'D', 'E', 'F', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	dedup = {'A', 'C', 'D', 'F', 0, 3, 4, 5, 6, 7, 10}

	s = SetOperation(original, dedup)
	s.get_difference()
	print(s.original_minus_dedup)
	