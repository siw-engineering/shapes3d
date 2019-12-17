"""Author: Christie J Purackal
email: christeejacobs@gmail.com
"""

import numpy as np
from utils import get_rotation_matrix


class Shape(object):
	"""Abstract shape class.
	Defines properties of shapes like position,
	orientation etc
	"""
	def __init__(self):
		
		self._x, self._y, self._z = 0,0,0
		self.roll, self.pitch, self.yaw = 0,0,0



	def set_pos(self, pos):
		if type(pos) not in (tuple, list):
			raise TypeError("Expected tuple or list, got %s"%(type(pos)))
		if len(pos) != 3:
			raise ValueError("Expected tuple or list of len 3, got len %s"%(len(pos)))

		self._x = pos[0]
		self._y = pos[1]
		self._z = pos[2]
		for i, (x,y,z) in enumerate(self._pc):
			self._pc[i] = pos[0]+x, pos[1]+y, pos[2]+z

	
	def rotate(self, theta=30, axis=0):
		rx, ry, rz = get_rotation_matrix(theta)
		if axis == 0:
			rm = rx
		elif axis == 1:
			rm = ry
		elif axis == 2:
			rm = rz
		else:
			raise ValueError("Invalid axis")

		for i, (x,y,z) in enumerate(self._pc):
			self._pc[i] = np.matmul(rm,np.array([x,y,z]).T)

	@property
	def pc(self):
		return self._pc
	


	@property
	def x(self):
		return self._x

	@property
	def y(self):
		return self._y

	@property
	def z(self):
		return self._z  

	@property
	def pos(self):
		return (self._x, self._y, self._z)



