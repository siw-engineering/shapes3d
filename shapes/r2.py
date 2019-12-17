"""Author: Christie J Purackal
email: christeejacobs@gmail.com
"""

import numpy as np
from shapes import Shape

class Rect(Shape):
	"""Rect PC generation function.
	# Arguments
	"""
	def __init__(self,l=10,b=10):
		super().__init__()
		self._pc = np.zeros((l*b,3))
		for i in range(l*b):
			self._pc[i,:] =  self._x + i%l, self._y + int(i/l), self._z
