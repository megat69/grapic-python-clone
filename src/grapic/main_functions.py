from typing import Union
import pygame

from grapic.main_class import Grapic


def win_init(title: str, dimension_x: int, dimension_y: int) -> None:
	"""
	Initializes the window with the given title and dimensions.
	:param title: The title of the window.
	:param dimension_x: The x dimension of the window.
	:param dimension_y: The y dimension of the window.
	"""
	Grapic(title, dimension_x, dimension_y)


def win_display() -> bool:
	"""
	Updates the window, returns whether the user wanted to quit.
	:return: Whether the user wants to leave the app.
	"""
	return Grapic.singleton().win_display()


def win_clear() -> None:
	"""
	Clears the contents of the window and fills the screen with the background color.
	"""
	return Grapic.singleton().win_clear()


def background_color(r: Union[int, float], g: Union[int, float], b: Union[int, float]) -> None:
	"""
	Sets the background color of the window to the given r, g, b values.
	All values should be integers between 0 and 255, or float values between 0 and 1.
	:param r: The red component of the color. Int between 0 and 255 or Float between 0 and 1.
	:param g: The green component of the color. Int between 0 and 255 or Float between 0 and 1.
	:param b: The blue component of the color. Int between 0 and 255 or Float between 0 and 1.
	"""
	# If the values are integers with correct values
	if all(isinstance(channel, int) for channel in (r, g, b)):
		# Sets the color if the values are in the correct range
		if all(0 <= channel <= 255 for channel in (r, g, b)):
			Grapic.singleton().background_color = [r, g, b]

		# Raises an exception if the values are not in the correct range
		else:
			raise ValueError(
				f"Background color could not be set, incorrect values received.\n"
				f"Int values should be within range [0, 255].\n"
				f"Got :\n"
				f"- r: {r}\n"
				f"- g: {g}\n"
				f"- b: {b}\n"
			)

	# If the values are floats with correct values
	elif all(isinstance(channel, float) for channel in (r, g, b)):
		# Sets the background color to be the integer version of the parameters if the colors are in the correct range
		if all(0 <= channel <= 1 for channel in (r, g, b)):
			Grapic.singleton().background_color = [e * 255 for e in (r, g, b)]

		# Raises an exception if the values are not in the correct range
		else:
			raise ValueError(
				f"Background color could not be set, incorrect values received.\n"
				f"Float values should be within range [0, 1].\n"
				f"Got :\n"
				f"- r: {r}\n"
				f"- g: {g}\n"
				f"- b: {b}\n"
			)

	# If the values are incorrect
	else:
		# Here raises an exception if not all values are ints or floats
		if not (all(isinstance(channel, int) for channel in (r, g, b)) and all(isinstance(channel, int) for channel in (r, g, b))):
			raise TypeError(
				f"Background color could not be set, incorrect types received.\n"
				f"r: {r} ({type(r)}), g: {g} ({type(g)}), b: {b} ({type(b)})"
			)


def color(r: Union[int, float], g: Union[int, float], b: Union[int, float]) -> None:
	"""
	Sets the foreground color of the window to the given r, g, b values.
	All values should be integers between 0 and 255, or float values between 0 and 1.
	:param r: The red component of the color. Int between 0 and 255 or Float between 0 and 1.
	:param g: The green component of the color. Int between 0 and 255 or Float between 0 and 1.
	:param b: The blue component of the color. Int between 0 and 255 or Float between 0 and 1.
	"""
	# If the values are integers with correct values
	if all(isinstance(channel, int) for channel in (r, g, b)):
		# Sets the color if the values are in the correct range
		if all(0 <= channel <= 255 for channel in (r, g, b)):
			Grapic.singleton().foreground_color = [r, g, b]

		# Raises an exception if the values are not in the correct range
		else:
			raise ValueError(
				f"Color could not be set, incorrect values received.\n"
				f"Int values should be within range [0, 255].\n"
				f"Got :\n"
				f"- r: {r}\n"
				f"- g: {g}\n"
				f"- b: {b}\n"
			)

	# If the values are floats with correct values
	elif all(isinstance(channel, float) for channel in (r, g, b)):
		# Sets the background color to be the integer version of the parameters if the colors are in the correct range
		if all(0 <= channel <= 1 for channel in (r, g, b)):
			Grapic.singleton().foreground_color = [e * 255 for e in (r, g, b)]

		# Raises an exception if the values are not in the correct range
		else:
			raise ValueError(
				f"Color could not be set, incorrect values received.\n"
				f"Float values should be within range [0, 1].\n"
				f"Got :\n"
				f"- r: {r}\n"
				f"- g: {g}\n"
				f"- b: {b}\n"
			)

	# If the values are incorrect
	else:
		# Here raises an exception if not all values are ints or floats
		if not (all(isinstance(channel, int) for channel in (r, g, b)) and all(isinstance(channel, int) for channel in (r, g, b))):
			raise TypeError(
				f"Color could not be set, incorrect types received.\n"
				f"r: {r} ({type(r)}), g: {g} ({type(g)}), b: {b} ({type(b)})"
			)


def elapsed_time() -> float:
	"""
	Returns the time elapsed since the beginning of the program in seconds.
	:return: The time elapsed since the start of the program in seconds.
	"""
	return pygame.time.get_ticks() / 1000


def rectangle(x1: int, y1: int, x2: int, y2: int):
	"""
	Draws a rectangle at the given coordinates.
	"""
	Grapic.singleton().rectangle(x1, y1, x2, y2)
