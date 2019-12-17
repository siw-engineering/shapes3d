
"""Author: Christie J Purackal
email: christeejacobs@gmail.com
"""

from shapes import Shape
import numpy as np
from utils import get_rotation_matrix
from shapes.r2 import Rect


class Cuboid(Shape):
	"""Cuboid PC generation function.
	# Arguments
	"""
	def __init__(self, l=10,b=5,w=5):
		super().__init__()
		self.l = l
		self.b = b
		self.w = w
		self._pc = np.zeros((l*b*w, 3))
		for j in range(0,l*b*w, l*b):
			for i in range(l*b):
				self._pc[i+j,:] =  self.x + i%l, self.y + int(i/l) , self.z + int(j/(l*b))


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






class Parallelepiped(Shape):
	""" PC generation function.
	# Arguments
	"""
	def __init__(self, l=10,b=5,w=5, theta=30):
		super().__init__()
		base = Rect(l=l, b=w)
		roof = Rect(l=l, b=w)
		s1 = Rect(l=w, b=b)
		s3 = Rect(l=w, b=b)
		
		s2 = Rect(l=l, b=b)
		s4 = Rect(l=l, b=b)


		#make the necessary quadrilateral transformations
		base.rotate(theta=90, axis=0)
		roof.rotate(theta=90, axis=0)

		s1.rotate(theta=270, axis=1)
		s3.rotate(theta=270, axis=1)

		s3.rotate(theta=theta, axis=2)
		s1.rotate(theta=theta, axis=2)
		
		#need to fix when theta > 90
		s3.set_pos([l-1,0,0])
		roof.set_pos([-b*np.cos(np.radians(90-theta)),b*np.sin(np.radians(90-theta)),0])



		self._pc = np.concatenate([base.pc, roof.pc, s1.pc, s3.pc], axis=0)



		
class trapezoidal_prism(Shape):
	""" PC generation function.
	# Arguments
	"""
	def __init__(self):
		raise NotImplementedError("Yet to be implemented")

class Rhombohedron(Shape):
	""" PC generation function.
	# Arguments
	"""
	def __init__(self, side=10, theta=30):
		self._pc = Parallelepiped(l=side,b=side,w=side,theta=theta).pc

class Sphere(Shape):
	"""Sphere PC generation function.
	# Arguments
		radius: radius of the the sphere.
	"""
	def __init__(self, radius=1):
		super().__init__()
		self.radius = radius

	def numpy(self):
		radius = self.radius
		sphere = np.zeros((2*180*radius*360, 3))
		circle = np.zeros((2*180*radius, 3))
		circle[:, 0] =  self.x + np.sin(np.radians([x for x in range(0,2*180*radius)]))
		circle[:, 1] =  self.y + np.cos(np.radians([x for x in range(0,2*180*radius)]))
		circle[:, 2] =	self.z 

		for z_theta in range(360):
			rx, _, _ = get_rotation_matrix(z_theta)
			for i, (x,y,z) in enumerate(circle):
				sphere[i + z_theta*360] = np.matmul(rx,np.array([x,y,z]).T)

		return sphere


class Cylinder(Shape):
	"""Cylinder PC generation function.
	# Arguments
		radius: radius of the the cylinder.
	"""
	def __init__(self, radius=5, length=10):
		super().__init__()
		self.radius = radius
		self.length = length



	def numpy(self):
		radius = self.radius
		length = self.length

		cylinder = np.zeros((2*180*radius*length,3))

		for l in range(0,2*180*radius*length, 2*180*radius):
			for i in range(2*180*radius):
				cylinder[i+l,:] = self.x + radius * np.sin(np.radians(i)), self.y + radius * np.cos(np.radians(i)), self.z + int(l/(2*180*radius)) 
		return cylinder
			
