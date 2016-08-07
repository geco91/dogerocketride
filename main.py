import ugfx
import pyb
import buttons

def display1():
	ugfx.display_image(0,0,'apps/apps/rootzoll~dogerocketride/1.gif')

def display2():
	ugfx.display_image(0,0,'apps/apps/rootzoll~dogerocketride/2.gif')

def display3():
	ugfx.display_image(0,0,'apps/apps/rootzoll~dogerocketride/3.gif')

buttons.init()

while not buttons.is_pressed("BTN_MENU"):
	display1()
	pyb.delay(500)
	display2()
	pyb.delay(500)
	display3()
	pyb.delay(500)