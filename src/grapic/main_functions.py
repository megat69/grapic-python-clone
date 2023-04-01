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
	return Grapic._singleton.win_display()


def win_clear() -> None:
	"""
	Clears the contents of the window and fills the screen with the background color.
	"""
	return Grapic._singleton.win_clear()
