# Imports grapic
import grapic

# Creates a new window
grapic.win_init("test", 400, 600)

# Loops until the user wants to stop
stop = False
while stop is False:
	# Clears the screen
	grapic.win_clear()

	# Updates the display and gets whether the user closed the window
	stop = grapic.win_display()
