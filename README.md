# CircuitPython Assignments

Below are descriptions of all the CircuitPython assignments I did. I used a Metro M0 Express and the software Mu. Mu ran our code, written in the CircuitPython language. The [CircuitPython Essentials](https://learn.adafruit.com/circuitpython-essentials) page on Adafruit's website was extremely helpful. I'm using Dr. Shields' Fritzing diagrams because I didn't make any. His github page can be found [here](https://github.com/DoctorShields).

## LED Fade
The goal of this assignment was to make an LED fade in and out continuously. I did so using the duty_cycle module and creating a PWM object for the LED. By changing the duty cycle on the LED's power, I was able to get the desired effect of a fading & brightening LED. My code can be found under [led_fade.py](https://github.com/rmiller85/CircuitPython/blob/master/led_fade.py).
##### Fritzing Model

## CircuitPython Servo
For this one, I had to make a servo move, controlled by touch-sensitive wires. There were two wires: one for each direction. I used a PWM object again, this one controlling a servo rather than an LED. The code for this one is at [circuitPython_servo.py](https://github.com/rmiller85/CircuitPython/blob/master/circuitPython_servo.py).

## circuitPython_lcd.py
Made an LCD screen display # of times a button had been pressed

## photo_interrupt.py
Made a counter of how many times a photo interrupter had been interrupted. Made a 4-second timer so that it is constantly looping, but only prints the number of interrupts once every 4 seconds.

## dist_sensor.py
Hooked an ultrasonic sensor up to my Metro. Made the onboard 
Metro RGB LED display different colors based on the reading from the sensor.

## rgb.py
Hoo boy, this was crazy. I made my own module with a class in it, called rgb. In the class, creatively named RGB, I made a few functions which set an RGB LED to different colors. This was a hard assignment, but pretty fun!

## hello_vs_code.py
This was my first introduction to VS Code. Basic stuff, just printing "Hello there!" every second. I also made it print "General Kenobi! You are a bold one..." in response, because I'm a big heckin nerd.