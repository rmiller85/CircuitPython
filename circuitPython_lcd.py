  #  lines 3-9 import all the junk we need

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from lcd.lcd import CursorMode

import time
from digitalio import DigitalInOut, Direction, Pull
import board

button = DigitalInOut(board.D2)
button.direction = Direction.INPUT  # sets the button pin for receiving input
button.pull = Pull.UP  # provides power for button

presses = 0  # creates a counter for how many times the button has been pressed

lcd = LCD(I2CPCF8574Interface(0x3F), num_rows=2, num_cols=16)

lcd.set_cursor_mode(CursorMode.LINE)  # Make the cursor visible as a line.

lcd.set_cursor_pos(0, 2)  # Sets position of cursor.
lcd.print("Booting up!")
time.sleep(.5)

while True:
    lcd.set_cursor_pos(0, 0)  # Sets position of cursor.
    lcd.print("Button Presses:")
    if not button.value:
        presses += 1  # shorter way of saying presses = presses + 1
    lcd.set_cursor_pos(1, 0)  # Sets position of cursor.
    lcd.print(str(presses))
    print(button.value)  # tells me if the button is getting pressed
    time.sleep(.01)  # stops it from looping a zillion times a second