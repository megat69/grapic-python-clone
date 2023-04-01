# Imports grapic
from grapic import *

# Creates a new window
win_init("test", 400, 600)
background_color(0.3, 0.2, 1.0)

# Loops until the user wants to stop
stop = False
while stop is False:
	# Clears the screen
	win_clear()

	# Updates the display and gets whether the user closed the window
	stop = win_display()
