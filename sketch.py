from p5 import *
from mover import Mover


mover_num = 10


def setup():
	size(850, 600)
	title("Art Generator")
	background(250)

	global movers
	movers = []
	for i in range(mover_num):
		movers.append(Mover())

def draw():
	# background(250)

	wind = Vector.from_angle((frame_count*PI)/120) * random_gaussian(0.8)

	for mover in movers:
		mover.apply_force(wind)
		mover.update()
		mover.show()

	if (frame_count == 600):
		save("/home/novawarrior42/Programs/art_generator/art/art.png")
		exit()
		

run()