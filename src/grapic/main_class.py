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

	def __init__(self, title: str, dimension_x: int, dimension_y: int):
		"""
		Creates an instance of the grapic class.
		This will contain all the code under the hood to make the library work.
		"""
		self.screen = pygame.display.set_mode((dimension_x, dimension_y))
		pygame.display.set_caption(title)

		# Defines the current color of the background and foreground
		self.background_color = [  0,   0,   0]
		self.foreground_color = [255, 255, 255]


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
