from time import sleep
from digitalio import DigitalInOut, Direction, Pull #pylint: disable=import-error
from random import randint

class FancyLED:

    counter = 0

    def __init__(self, p1, p2, p3):
        print("I exist")
        self.p1 = DigitalInOut(p1)
        self.p1.direction = Direction.OUTPUT
        self.p2 = DigitalInOut(p2)
        self.p2.direction = Direction.OUTPUT
        self.p3 = DigitalInOut(p3)
        self.p3.direction = Direction.OUTPUT

    def alternate(self):
            for i in range(0,4)
                self.p1.value = True
                self.p2.value = False
                self.p3.value = True
                sleep(0.5)
                self.p1.value = False
                self.p2.value = True
                self.p3.value = False
                sleep(0.5)

    def blink(self):
            self.p1.value = True
            self.p2.value = True
            self.p3.value = True
            sleep(1)
            self.p1.value = False
            self.p2.value = False
            self.p3.value = False
            sleep(1)
            self.p1.value = True
            self.p2.value = True
            self.p3.value = True
            sleep(1)

    def chase(self):
            self.p1.value = False
            self.p2.value = False
            self.p3.value = False
            sleep(.2)
            self.p1.value = True
            self.p2.value = False
            self.p3.value = False
            sleep(.2)
            self.p1.value = True
            self.p2.value = True
            self.p3.value = False
            sleep(.2)
            self.p1.value = False
            self.p2.value = True
            self.p3.value = True
            sleep(.2)
            self.p1.value = False
            self.p2.value = False
            self.p3.value = True
            sleep(.2)

    def sparkle(self):
            for counter in range(0,25):
                    p1_rand = randint(1,2)
                    p2_rand = randint(1,2)
                    p3_rand = randint(1,2)
                    if p1_rand == 1:
                            self.p1.value = True
                    else:
                            self.p1.value = False
                    if p2_rand == 1:
                            self.p2.value = True
                    else:
                            self.p2.value = False
                    if p3_rand == 1:
                            self.p3.value = True
                    else:
                            self.p3.value = False
                    counter += 1
                    sleep(.05)
                    print(counter)