#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.ev3devices import Motor


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3data = EV3Brick()
sensordata = ColorSensor(Port.1)
motordata = Motor(Port.A)

motordata.run_forever()

while True:
    szin = sensor.color()
    
    if szin == "blue":
        motordata.stop()
        ev3.speaker.beep()

    while True:
        if szin != "blue":
            motordata.run_forever()
    
