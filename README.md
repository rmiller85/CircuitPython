# CircuitPython Assignments

Below are descriptions of all the CircuitPython assignments I did. I used a Metro M0 Express and the software Mu (except I started using VS Code a little later.). Mu ran my code (until it didn't), written in the CircuitPython language. The [CircuitPython Essentials](https://learn.adafruit.com/circuitpython-essentials) page on Adafruit's website was extremely helpful. I'm using a whole bunch of other people's Fritzing models. Now don't get the wrong idea, I *would* make my own, but I didn't. So here we are. Unfortunately, this means that some pins won't be the same, ~~but if you can't deal with it all I can say is git gud~~ but I trust *YOU* to figure it out! I'm crediting all the Fritzings I steal and providing links to their Githubs. Here's the list right now.

[Dr Shields](https://github.com/DoctorShields)

add more people if you use them

## USE CIRCUITPYTHON ESSENTIALS! IT SAVED MY ASS A HUNDRED TIMES!
Seriously, bookmark that link **_right now!_** It gives you simple instructions on how tons of stuff works. The farther in to these assignments you get, the less useful this is, but, at least for a long while, it's true to its name: essential.

## LED Fade
The goal of this assignment was to make an LED fade in and out continuously. I did so using the duty_cycle module and creating a PWM object for the LED. By changing the duty cycle on the LED's power, I was able to get the desired effect of a fading & brightening LED. My code can be found under [led_fade.py](https://github.com/rmiller85/CircuitPython/blob/master/led_fade.py).
#### Fritzing Model from Dr Shields

## CircuitPython Servo
For this one, I had to make a servo move, controlled by touch-sensitive wires. There were two wires: one for each direction. I used a PWM object again, this one controlling a servo rather than an LED. One of the great things about our Metros is that the `touchio` module did basically all the touch stuff for us. We only had to make a touch object and check its value to see if it was being pressed. For example, if I made a touch object called `touchL`, I could check if it was being pressed with `touchL.value`. The code for this one is at [circuitPython_servo.py](https://github.com/rmiller85/CircuitPython/blob/master/circuitPython_servo.py).
#### Fritzing Model from Dr Shields

## CircuitPython LCD
Now I had to wire up an LCD screen and a button. The LCD screen would display how many times the button had been pressed. LCD screens, of course, have an ungodly amount of things you have to wire up, but I was saved by an LCD backpack, which cut the wires down to just four! I had to download a bunch of modules for using LCDs on CircuitPython, but it wasn't too much trouble. I used a simple function that added one to the `presses` variable whenever the button was pressed, then printed that as a `str` to the LCD. The code is under [circuitPython_lcd.py](https://github.com/rmiller85/CircuitPython/blob/master/circuitPython_lcd.py)
#### Fritzing Model

## CircuitPython Photointerrupters
This was a real doozy. I had to wire up a photo interrupter and get it to count how many times it was interrupted in 4 seconds. It would count down from 4 while counting interrupts. Simple, right? Just use `time.sleep()`! Except it has to be counting interrupts while it counts down from 4. To put it simply, I had to make a timer, separate from the loop, that would activate a `print` function every 4 seconds. For this, I used the `monotonic()` function from the `time` module. Here's the snippet of my code that uses this.

```python
max = 4
start = time.monotonic()
while True:
    remaining = max + start - time.monotonic()
    # When countdown ends, prints value
    if remaining <= 0:
        print("Interrupts:", str(interrupts))
        max += 4
        interrupts = 0
```
So I set the max as 4 and store the current time as `start`. Then, we have the loop. I left out the interrupt counter for this, but I'll get to that in a hot second. I then create a variable, `remaining`, which tracks how much time is left. Every time that the function loops, `remaining` is changed to `max` (which is 4) plus `start` (the time when the code was started) minus `time.monotonic()` (the current time). This ends up setting `remaining` as `max` minus how much time has elapsed since we recorded `start`. It's going to be looping at warp speed, counting down constantly, until `remaining` reaches zero. Then, it prints the number of interrupts, sets `max` to itself plus 4 (It will become 8, then when the timer reaches 8, it will become 12, and so on.), and resets `interrupts` to zero.

Alright, hope you got all that. It's weird, I know. Now, for the interrupt counting. Don't worry, this is much simpler. Here's the code.

```python
while True:
    interpt_state = interpt_pin.value
    if interpt_state and not last_state:
        interrupts += 1
    last_state = interpt_state
```

First, I create the variable `interpt_state` and set it to the current value of the photo interrupter: `True` or `False`. The `if` statement under it basically means, "if it's being interrupted, but wasn't being interrupted the last time I checked." This is so that it doesn't just rocket up if you hold something in it for a while. If that's `True`, it adds one to the interrupt counter, `interrupts`. Finally, I set `last_state` to `interpt_state`. In layman's terms, the next time that it loops, the variable `last_state` will be equal to whatever it is right now. We aren't checking for just whether or not it's *currently* being interrupted, we're checking for whether or not it just got interrupted. Sorry if that didn't make a ton of sense.
#### Fritzing Model

## CircuitPython Distance Sensor
Hooked an ultrasonic sensor up to my Metro. Made the onboard Metro RGB LED display different colors based on the reading from the sensor.

## Classes, Objects, and Modules
Hoo boy, this was crazy. I made my own module with a class in it, called rgb. In the class, creatively named RGB, I made a few functions which set an RGB LED to different colors. This was a hard assignment, but pretty fun!

## Hello VS Code
This was my first introduction to VS Code. Basic stuff, just printing "Hello there!" every second. I also made it print `General Kenobi! You are a bold one...` in response, because I'm a big heckin nerd. Code's at [hello_vs_code.py](https://github.com/rmiller85/CircuitPython/blob/master/hello_vs_code.py).

## FancyLED
