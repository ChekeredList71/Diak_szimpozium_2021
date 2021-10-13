#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.ev3devices import Motor


ev3data = EV3Brick()
sensordata = ColorSensor(Port.S1)
motordata = Motor(Port.A)

#Program része
motordata.run(-150)

while True:

    if (str(sensordata.color()) == "Color.RED"):
        print("ok")
        motordata.brake()
        ev3data.speaker.beep()