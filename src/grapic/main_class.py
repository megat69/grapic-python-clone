import pygame


class Grapic:
	_singleton = None

	def __new__(cls, *args, **kwargs):
		"""
		Creates a singleton of the class.
		"""
		if cls._singleton is None:
			cls._singleton = super().__new__(cls)
		return cls._singleton


	@classmethod
	def singleton(cls):
		"""
		Returns the singleton instance of the class.
		"""
		return cls._singleton


	def __init__(self, title: str, dimension_x: int, dimension_y: int):
		"""
		Creates an instance of the grapic class.
		This will contain all the code under the hood to make the library work.
		"""
		pygame.init()

		if isinstance(dimension_x, int) and isinstance(dimension_y, int) and dimension_x > 0 and dimension_y > 0:
			self.window_size = (dimension_x, dimension_y)
			self.screen = pygame.display.set_mode(self.window_size)
		else:
			raise TypeError(
				f"'dimension_x' and 'dimension_y' should be positive integers, got "
				f"dimension_x = {dimension_x} ({type(dimension_x)}) and "
				f"dimension_y = {dimension_y} ({type(dimension_y)})."
			)

		if isinstance(title, str):
			pygame.display.set_caption(title)
		else:
			raise TypeError(f"'title' parameter must be a string, got {title} ({type(title)}).")

		# Defines the current color of the background and foreground
		self.background_color = [  0,   0,   0]
		self.foreground_color = [255, 255, 255]


	def _invertY(self, val: int) -> int:
		"""
		Turns the coordinate system into a y+ coordinate system
		:param val: A y value to convert.
		"""
		return self.window_size[1] - val


	def win_display(self) -> bool:
		"""
		Updates the window, returns whether the user wanted to quit.
		:return: Whether the user wants to leave the app.
		"""
		pygame.display.update()
		return any(
			event.type == pygame.QUIT
			for event in pygame.event.get()
		) or pygame.key.get_pressed()[pygame.K_q] or pygame.key.get_pressed()[pygame.K_ESCAPE]


	def win_clear(self) -> None:
		"""
		Clears the contents of the window and fills the screen with the background color.
		"""
		self.screen.fill(self.background_color)


	def rectangle(self, x1: int, y1: int, x2: int, y2: int):
		"""
		Draws a rectangle at the given coordinates.
		"""

		pygame.draw.rect(
			self.screen,
			self.foreground_color,
			(x1, y1, abs(x1 - x2), abs(y1 - y2)),
			1
		)


	def rectangle_fill(self, x1: int, y1: int, x2: int, y2: int):
		"""
		Draws a rectangle filled with the active color at the given coordinates.
		"""
		pygame.draw.rect(
			self.screen,
			self.foreground_color,
			(x1, y1, abs(x1 - x2), abs(y1 - y2))
		)


	def line(self, x1: int, y1: int, x2: int, y2: int):
		"""
		Draws a line from (x1, y1) to (x2, y2).
		"""
		pygame.draw.line(
			self.screen,
			self.foreground_color,
			(x1, self._invertY(y1)),
			(x2, self._invertY(y2))
		)


	def circle(self, x: int, y: int, radius: int):
		"""
		Draws a circle with the given radius at the given coordinates.
		"""
		pygame.draw.circle(
			self.screen,
			self.foreground_color,
			(x, self._invertY(y)),
			radius,
			1
		)


	def circle_fill(self, x: int, y: int, radius: int):
		"""
		Draws a circle filled with the active color with the given radius at the given coordinates.
		"""
		pygame.draw.circle(
			self.screen,
			self.foreground_color,
			(x, self._invertY(y)),
			radius
		)
