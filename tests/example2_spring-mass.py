from dataclasses import dataclass
from math import sqrt

from Tools.demo.vector import Vec

# Imports grapic
from grapic import *


# Creates a new window
DIMW = 512
PARTICLE_SIZE = 10
DAMPENING = 0.999
win_init("Spring-mass model", DIMW, DIMW)


@dataclass(slots=True)
class Vec2:
	x: float
	y: float

	def __add__(self, other):
		if isinstance(other, Vec2):
			return Vec2(self.x + other.x, self.y + other.y)

	def __sub__(self, other):
		if isinstance(other, Vec2):
			return Vec2(self.x - other.x, self.y - other.y)


	def __mul__(self, other):
		if isinstance(other, (float, int)):
			return Vec2(self.x * other, self.y * other)


	def __rmul__(self, other):
		if isinstance(other, (float, int)):
			return Vec2(self.x * other, self.y * other)


	def __truediv__(self, other):
		if isinstance(other, (float, int)):
			return Vec2(self.x / other, self.y / other)


	@classmethod
	def distance(cls, vec1, vec2):
		return sqrt((vec2.x - vec1.x) ** 2 + (vec2.y - vec1.y) ** 2)


@dataclass(slots=True)
class Particle:
	pos: Vec2
	force: Vec2
	velocity: Vec2
	mass: float


@dataclass
class Spring:
	stiffness: float
	length: float
	particle1: Particle
	particle2: Particle


@dataclass
class World:
	dt: float
	particles: list[Particle]
	springs: list[Spring]


def update(world: World):
	"""
	Updates the position of the particles.
	:param world: The game world.
	"""
	# Updates the particles' gravity
	for particle in world.particles:
		if particle.mass > 0:
			particle.force = Vec2(0, -9.81)

	# Updates the springs
	for spring in world.springs:
		distance = Vec2.distance(spring.particle1.pos, spring.particle2.pos)
		direction = (spring.particle1.pos - spring.particle2.pos) / (distance + 1e-5)

		# Adds some force to the particles
		force = spring.stiffness * (distance - spring.length) * direction * DAMPENING
		spring.particle1.force += force
		spring.particle2.force -= force


	# Updates the particles' positions
	for particle in world.particles:
		if particle.mass > 0:
			particle.velocity += particle.force * world.dt
			particle.pos += particle.velocity * world.dt



def draw(world: World):
	"""
	Draws the particles in the world.
	:param world: The game world.
	"""
	# Draws the springs
	for spring in world.springs:
		line(spring.particle1.pos.x, spring.particle1.pos.y, spring.particle2.pos.x, spring.particle2.pos.y)

	# Draws the particles
	for particle in world.particles:
		if particle.mass <= 0:
			color(1.0, 0.0, 0.0)
		else:
			color(1.0, 1.0, 1.0)
		circle_fill(particle.pos.x, particle.pos.y, PARTICLE_SIZE)


def main():
	# Creates a new world
	world = World(0, [
		Particle(
			Vec2(DIMW / 2, DIMW / 2),
			Vec2(0, 0), Vec2(0, 0), 0
		),
		Particle(
			Vec2(DIMW / 2 + 100, DIMW / 2),
			Vec2(0, 0), Vec2(0, 0), 1
		)
	], [])
	world.springs.append(
		Spring(500, Vec2.distance(world.particles[0].pos, world.particles[1].pos), world.particles[0], world.particles[1])
	)
	last_time = 0

	# Loops until the user wants to stop
	stop = False
	while stop is False:
		# Clears the screen
		win_clear()

		# Computes the delta time
		world.dt = elapsed_time() - last_time
		last_time = elapsed_time()

		# Updates all the particles
		update(world)

		# Draws all the particles and springs
		draw(world)

		# Updates the display and gets whether the user closed the window
		stop = win_display()


if __name__ == "__main__":
	main()
