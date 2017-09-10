#--------------------------------------------------------------------
# particle.py
#--------------------------------------------------------------------

import sys
import math
#--------------------------------------------------------------------

class Particle:
	# Create the particle at position (x, y) with velocity (vx,vy).
	def __init__(self, x0, y0, vx0, vy0):
		self.x0 = x0
		self.y0 = y0
		self.vx0 = vx0
		self.vy0 = vy0

def main():
	x = float(sys.argv[1])


