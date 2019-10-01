import board
from time import sleep
from digitalio import DigitalInOut, Direction, Pull

class FancyLED:
    def __init__(self, p1, p2, p3)
        self.p1 = DigitalInOut(p1)
        p1.direction = Direction.OUTPUT
        self.p2 = DigitalInOut(p2)
        p2.direction = Direction.OUTPUT
        self.p3 = DigitalInOut(p3)
        p3.direction = Direction.OUTPUT
    def alternate():
        while True:
            p1.value = True
            p2.value = False
            p3.value = True
            sleep(1.5)
            p1.value = False
            p2.value = True
            p3.value = False
            sleep(1.5)
    def blink():
        while True:
            p1.value = True
            p2.value = True
            p3.value = True
            sleep(1)
            p1.value = False
            p2.value = False
            p3.value = False
            sleep(.1)
    def chase():
        while True:
            p1.value = False
            p2.value = False
            p3.value = False
            sleep(.2)
            p1.value = True
            p2.value = False
            p3.value = False
            sleep(.2)
            p1.value = True
            p2.value = True
            p3.value = False
            sleep(.2)
            p1.value = False
            p2.value = True
            p3.value = True
            sleep(.2)
            p1.value = False
            p2.value = False
            p3.value = True
            sleep(.2)
    def sparkle():
        while True:
            p1.value = True
            p2.value = True
            p3.value = False
            sleep(.05)
            p1.value = True
            p2.value = False
            p3.value = True
            sleep(.05)
            p1.value = False
            p2.value = False
            p3.value = False
            sleep(.05)
            p1.value = False
            p2.value = True
            p3.value = False
            sleep(.05)
            p1.value = False
            p2.value = True
            p3.value = True
            sleep(.05)