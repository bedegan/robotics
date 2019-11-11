from ev3dev.ev3 import *
from time import sleep

# Connect EV3 color and touch sensors to any sensor ports
cl = ColorSensor() 
ts = TouchSensor()
mA = LargeMotor('outA') # motor that runs claw
mB = LargeMotor('outB')	# mB = right motor
mC = LargeMotor('outC') # mC = left motor

# Put the color sensor into COL-COLOR mode.
cl.mode='COL-COLOR'

UNKNOWN = 0
BLACK = 1
BLUE = 2
GREEN = 3
YELLOW = 4
RED = 5
WHITE = 6
BROWN = 7



while True:
	if ts.value():
		findColor = (cl.value())
		print("findColor=" + str(findColor))
		Sound.speak(cl.value()).wait()
		sleep(1)
		break

# move forward to scan the lined up balls (balls lined up on the side of robot)
mB.run_forever(speed_sp=-50, stop_action ="brake")
mC.run_forever(speed_sp=-50, stop_action ="brake")

while not ts.value(): 
	curr_color = cl.value()
	print(curr_color)

	if curr_color == BLACK:
		mB.run_forever(speed_sp=-50, stop_action ="brake")
		mC.run_forever(speed_sp=-50, stop_action ="brake")
		sleep(.5)
		continue

	elif (curr_color != findColor):
		# go around the balls
		mB.run_forever(speed_sp=100) #Go back
		mC.run_forever(speed_sp=100)
		Sound.beep()
		sleep(3)
		mB.run_forever(speed_sp=-100) #Turn Right
		mC.run_forever(speed_sp=100)
		Sound.beep()
		sleep(2)
		mB.run_forever(speed_sp=-100) #Go forwards
		mC.run_forever(speed_sp=-100)
		Sound.beep()
		sleep(3.5)
		mB.run_forever(speed_sp=100) #Turn left
		mC.run_forever(speed_sp=-100)
		Sound.beep()
		sleep(1.5)
		mB.run_forever(speed_sp=-100) #Go forwards
		mC.run_forever(speed_sp=-100)
		Sound.beep()
		sleep(3)
		mB.run_forever(speed_sp=100) #Turn left
		mC.run_forever(speed_sp=-100)
		Sound.beep()
		sleep(2)
		mB.run_forever(speed_sp=-100) #Go forwards
		mC.run_forever(speed_sp=-100)
		Sound.beep()
		sleep(5.75)
		Sound.beep()
		mB.run_forever(speed_sp=-70) #Turn Right
		mC.run_forever(speed_sp=70)
		sleep(2.25)
		mB.stop(stop_action='coast')
		mC.stop(stop_action='coast')
		continue





	elif curr_color == findColor:
		mB.stop(stop_action='brake')   # stop motors when ball is found
		mC.stop(stop_action='brake')

		# move claw to do something
		mA.run_to_rel_pos(position_sp=90, speed_sp=1050, stop_action="brake")
		sleep(1)
		mA.run_to_rel_pos(position_sp=-90, speed_sp=1050, stop_action="brake")
		sleep(1)

	else:
		mB.run_forever(speed_sp=-50, stop_action ="brake")
		mC.run_forever(speed_sp=-50, stop_action ="brake")



# if correct color ball isn't found after certain amount of time, go backwards to starting place
#mB.run_forever(speed_sp=-60, stop_action ="brake")
#mC.run_forever(speed_sp=-60, stop_action ="brake")
#sleep(4)
mC.stop()
mB.stop()
Sound.beep()