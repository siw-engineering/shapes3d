import numpy as np


RX = np.zeros((3,3))
RY = np.zeros((3,3))
RZ = np.zeros((3,3))

def get_rotation_matrix(theta):
	RX[0,0] = 1
	RX[1,1] = np.cos(np.radians(theta))
	RX[1,2] = -np.sin(np.radians(theta))
	RX[2,1] = np.sin(np.radians(theta))
	RX[2,2] = np.cos(np.radians(theta))

	RY[1,1] = 1
	RY[0,0] = np.cos(np.radians(theta))
	RY[0,2] = np.sin(np.radians(theta))
	RY[2,0] = -np.sin(np.radians(theta))
	RY[2,2] = np.cos(np.radians(theta))

	RZ[2,2] = 1
	RZ[0,0] = np.cos(np.radians(theta))
	RZ[0,1] = -np.sin(np.radians(theta))
	RZ[1,0] = np.sin(np.radians(theta))
	RZ[1,1] = np.cos(np.radians(theta))

	return RX, RY, RZ