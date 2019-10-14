from time import sleep
from fancyLED import FancyLED

fancy1 = FancyLED(2,3,4)
fancy2 = FancyLED(5,6,7)

while True:
    fancy1.alternate()
    fancy2.blink()
    sleep(5)
    fancy1.chase()
    fancy2.sparkle()
    sleep(4)