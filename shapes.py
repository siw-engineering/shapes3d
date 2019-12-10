"""Author: Christie J Purackal
email: christeejacobs@gmail.com
"""

import numpy as np

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


class Cube(Shape):
	"""Cube PC generation function.
	# Arguments
		side: Side length of the Cube.
	"""
	def __init__(self, side=5):
		super().__init__()
		self.side = side
		self._cube = np.zeros((side*side*side, 3))

	
	def numpy(self):
		side = self.side
		for j in range(0,side*side*side, side*side):
			for i in range(side*side):
				self._cube[i+j,:] =  self.x + i%side, self.y + int(i/side) , self.z + int(j/(side*side))
		return self._cube



class Cuboid(Shape):
	""" PC generation function.
	# Arguments
	"""
	def __init__(self, b,h,l):
		self.b = b
		self.h = h
		self.l = l
		self._cuboid = np.zeros((b*h*l, 3))


	def numpy(self):
		b = self.b
		h = self.h
		l = self.l

		for j in range(0,b*h*l, b*h):
			for i in range(b*h):
				self._cuboid[i+j,:] =  self.x + i%b, self.y + int(i/h) , self.z + int(j/(b*h))
		return self._cuboid


class Parallelepiped(Shape):
	""" PC generation function.
	# Arguments
	"""
	def __init__(self):
		raise NotImplementedError("Yet to be implemented")

class Trapezium(Shape):
	""" PC generation function.
	# Arguments
	"""
	def __init__(self):
		raise NotImplementedError("Yet to be implemented")

class Rhombohedron(Shape):
	""" PC generation function.
	# Arguments
	"""
	def __init__(self, l,b,w):
		raise NotImplementedError("Yet to be implemented")


class Sphere(Shape):
	"""Sphere PC generation function.
	# Arguments
		radius: radius of the the sphere.
	"""
	def __init__(self, radius=1):
		raise NotImplementedError("Yet to be implemented")
		# cords = np.zeros((0,3))
		# r = 1
		# for z_angle in range(0,360):
		# 	xyz = np.zeros((360,3))
		# 	y = r * np.sin(np.radians([x for x in range(0,360)]))
		# 	x = r * np.cos(np.radians([x for x in range(0,360)]))
			
		# 	xyz[:,0] = x 
		# 	xyz[:,1] = y
			
			
		# 	cords = np.concatenate([cords, xyz], axis=0)	

class Cylinder(Shape):
	"""Cylinder PC generation function.
	# Arguments
		radius: radius of the the cylinder.
	"""
	def __init__(self, radius=5, length=10):
		self.radius = radius
		self.length = length



	def numpy(self):
		radius = self.radius
		length = self.length

		cylinder = np.zeros((2*180*radius*length,3))

		for l in range(0,2*180*radius*length, 2*180*radius):
			for i in range(2*180*radius):
				cylinder[i+l,:] = radius * np.sin(np.radians(i)), radius * np.cos(np.radians(i)), int(l/(2*180*radius)) 
			print (int(l/(2*180*radius)))
		return cylinder
			

