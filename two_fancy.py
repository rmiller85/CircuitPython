from fancyLED import FancyLED

fancy1 = FancyLED(2,3,4)
fancy2 = FancyLED(5,6,7)

while True:
    fancy1.alternate()
    fancy1.chase()
    fancy2.blink()
    fancy2.sparkle()