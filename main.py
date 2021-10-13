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
motordata.run(50)

while True:
    szin = sensordata.color()
    
    if szin == "red":
        motordata.brake()
        ev3data.speaker.beep()
    else:
        while szin != "red":
                motordata.run(50)
                szin = sensordata.color()

    
