from p5 import *


class Mover:

	def __init__(self):
		self.loc = Vector(random_uniform(width, 0), random_uniform(height, 0))
		self.vel = Vector(random_uniform(10, -10), random_uniform(10, -10))
		self.acl = Vector(0,0)

		self.size = random_uniform(15, 4)
		self.mass = self.size / random_uniform(2, 1)

	def update(self):
		self.vel += self.acl
		self.loc += self.vel
		self.at_side()

		self.acl *= 0

	def at_side(self):
		if (self.loc.x <= 0):
			self.loc.x = 0
			self.vel.x *= -1

		if (self.loc.x >= width):
			self.loc.x = width
			self.vel.x *= -1

		if (self.loc.y <= 0):
			self.loc.y = 0
			self.vel.y *= -1

		if (self.loc.y >= height):
			self.loc.y = height
			self.vel.y *= -1

	def apply_force(self, f):
		force = f / self.mass
		self.acl += force

	def show(self):
		fill(random_uniform(255, 100), random_uniform(200, 0), random_uniform(150, 50))
		no_stroke()

		wiggle = self.size * 0.2
		ellipse(self.loc, self.size + random_uniform(wiggle, -wiggle), \
			self.size + random_uniform(wiggle, -wiggle))
		