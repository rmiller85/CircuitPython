from time import sleep
from fancyLED import FancyLED
import board

fancy1 = FancyLED(board.D2, board.D3, board.D4)
fancy2 = FancyLED(board.D5, board.D6, board.D7)

while True:
    print("It just works")
    fancy1.alternate()
    fancy2.blink()
    fancy1.chase()
    fancy2.sparkle()
    print("Little lies, stunning shows, people buy, money flows!")
    sleep(3)