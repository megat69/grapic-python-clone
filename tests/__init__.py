from math import sin
import pygame

# Imports grapic
from grapic import *

# Creates a new window
DIMW = 512
RECTANGLE_SIZE = 40
win_init("test", DIMW, DIMW)

# Loops until the user wants to stop
stop = False
while stop is False:
	# Clears the screen
	background_color(0.3, 0.2, abs(sin(elapsed_time())))
	win_clear()

	# Draws a rectangle at the center of the screen
	if pygame.key.get_pressed()[pygame.K_r]:
		color(0, 0, 0)
		rectangle_fill(
			DIMW // 2 - RECTANGLE_SIZE, DIMW // 2 - RECTANGLE_SIZE,
			DIMW // 2 + RECTANGLE_SIZE, DIMW // 2 + RECTANGLE_SIZE
		)
	else:
		color(1.0, 1.0, 1.0)
		rectangle(
			DIMW // 2 - RECTANGLE_SIZE, DIMW // 2 - RECTANGLE_SIZE,
			DIMW // 2 + RECTANGLE_SIZE, DIMW // 2 + RECTANGLE_SIZE
		)

	# Updates the display and gets whether the user closed the window
	stop = win_display()
