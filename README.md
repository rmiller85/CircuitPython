# CircuitPython Assignments

Below are descriptions of all the CircuitPython assignments I did. I used a Metro M0 Express and the software Mu. Mu ran our code, written in the CircuitPython language. The [CircuitPython Essentials](https://learn.adafruit.com/circuitpython-essentials) page on Adafruit's website was extremely helpful. I'm using Dr. Shields' Fritzing diagrams because I didn't make any. His github page can be found [here](https://github.com/DoctorShields).

## LED Fade
The goal of this assignment was to make an LED fade in and out continuously. I did so using the duty_cycle module and creating a PWM object for the LED. By changing the duty cycle on the LED's power, I was able to get the desired effect of a fading & brightening LED. My code can be found under [led_fade.py](https://github.com/rmiller85/CircuitPython/blob/master/led_fade.py).
#### Fritzing Model

## CircuitPython Servo
For this one, I had to make a servo move, controlled by touch-sensitive wires. There were two wires: one for each direction. I used a PWM object again, this one controlling a servo rather than an LED. One of the great things about our Metros is that the `touchio` module did basically all the touch stuff for us. We only had to make a touch object and check its value to see if it was being pressed. For example, if I made a touch object called `touchL`, I could check if it was being pressed with `touchL.value`. The code for this one is at [circuitPython_servo.py](https://github.com/rmiller85/CircuitPython/blob/master/circuitPython_servo.py).
#### Fritzing Model

## CircuitPython LCD
Now I had to wire up an LCD screen and a button. The LCD screen would display how many times the button had been pressed. LCD screens, of course, have an ungodly amount of things you have to wire up, but I was saved by an LCD backpack, which cut the wires down to just four! I had to download a bunch of modules for using LCDs on CircuitPython, but it wasn't too much trouble. I used a simple function that added one to the `presses` variable whenever the button was pressed, then printed that as a `str` to the LCD. The code is under [circuitPython_lcd.py](https://github.com/rmiller85/CircuitPython/blob/master/circuitPython_lcd.py)
#### Fritzing Model

## CircuitPython Photointerrupters
For this assignment, I had to wire up a photo interrupter and get it to count how many times it was interrupted in 4 seconds. It would count down from 4 while counting interrupts. Here's the trick

## CircuitPython Distance Sensor
Hooked an ultrasonic sensor up to my Metro. Made the onboard 
Metro RGB LED display different colors based on the reading from the sensor.

## Classes, Objects, and Modules
Hoo boy, this was crazy. I made my own module with a class in it, called rgb. In the class, creatively named RGB, I made a few functions which set an RGB LED to different colors. This was a hard assignment, but pretty fun!

## Hello VS Code
This was my first introduction to VS Code. Basic stuff, just printing "Hello there!" every second. I also made it print "General Kenobi! You are a bold one..." in response, because I'm a big heckin nerd. Code's at [hello_vs_code.py](https://github.com/rmiller85/CircuitPython/blob/master/hello_vs_code.py).

## FancyLED
