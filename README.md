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

First, I create the variable `interpt_state` and set it to the current value of the photo interrupter: `True` or `False`. The `if` statement under it basically means, "if it's being interrupted, but wasn't being interrupted the last time I checked." This is so that it doesn't just rocket up if you hold something in it for a while. If that's `True`, it adds one to the interrupt counter, `interrupts`. Finally, I set `last_state` to `interpt_state`. In layman's terms, the next time that it loops, the variable `last_state` will be equal to whatever it is right now. We aren't checking for just whether or not it's *currently* being interrupted, we're checking for whether or not it just got interrupted. Sorry if that didn't make a ton of sense. Full code's [here](https://github.com/rmiller85/CircuitPython/blob/master/photo_interrupt.py).
#### Fritzing Model

## CircuitPython Distance Sensor
This was pretty fun. I had to make the onboard LED change color based on a reading from an ultrasonic sensor. Unfortunately, most of our ultrasonic sensors are pretty much junk, but hey, you work with what you got. The neopixel module on Adafruit's website wasn't actually terribly helpful, unfortunately. I had to download a new module for the ultrasonic sensor called `adafruit_hcsr04`. It had lots of fun code that looks very scary, like how you create an object for your sensor: `adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)`. *Spooky*. Oh yeah, I also just made two new pins on that line that get used for the sensor. 

At the beginning of my loop, I use the function `distance`, included in that weird `hcrs04 or whatever` module, to get a reading from my sensor. Then, I print the value to the Serial Monitor just so that I can see if it's really messed up, like giving me 872.7 when I'm pointing it at something two inches away (yes, that kind of thing happened quite a bit). This is when I discovered that our sensors are....strange. I was getting some seriously bizarre readings. Turns out, my sensor was (probably) the problem. So of course I did the noble thing and put it back in the bin, because "Someone might want it." I'm sure the next person who used it was delighted. Seriously, I don't know what I was thinking in retrospect. Oh yeah, this happened twice in a row, too, if I remember correctly.

So anyway, after the inevitably f-ed up distance was printed, the code moved on the bulk of the "weird s**t". I used the `map_range` function from the `simpleio` module to get my r, g, & b values to go up or down with the distance. Here's that code.

```python
if sonarValue < 5:
    r = 255
    b = 0
    g = 0
if sonarValue <= 20 and sonarValue > 0:
    r = simpleio.map_range(sonarValue, 0, 20, 255, 0)
    b = simpleio.map_range(sonarValue, 5, 20, 0, 255)
    g = simpleio.map_range(sonarValue, 20, 35, 0, 255)
if sonarValue > 20 and sonarValue < 35:
    r = simpleio.map_range(sonarValue, 0, 20, 255, 0)
    b = simpleio.map_range(sonarValue, 35, 20, 0, 255)
    g = simpleio.map_range(sonarValue, 20, 35, 0, 255)
if sonarValue > 35:
    r = 0
    b = 0
    g = 255
```

After it runs all this code, it uses the `fill()` function from the `neopixel` module to set the color. [Here's the full code.](https://github.com/rmiller85/CircuitPython/blob/master/dist_sensor.py)

## Classes, Objects, and Modules
Hoo boy, this was crazy. I was obviously not new to the prospect of using modules and functions inside them, but now, I had to make my own! Turns out, it's not too terribly complicated. Pretty wack, but not some kind of insurmountable hurdle. Our goal was to make a `class` called `RGB` inside a file, `rgb.py`. This would have a bunch of functions that make the LED turn different colors. I used `PWM`s and `duty_cycle` again. For each function, I would print the color name and then activate the LED. Oh yeah, when you make an `RGB` object, you have to set the pins for `r`, `g`, & `b`. Here's an example: my `blue()` function.

```
def blue(self):
    print("blue")
    self.R.duty_cycle = self.full
    self.G.duty_cycle = self.full
    self.B.duty_cycle = 0
```
It takes `self` as an argument, which is just saying that the LED is what it's doing the function to. Then it turns on the `B` part of the LED object that our mysterious user has defined. Now, you might notice one key error in the logic. It turns on everything *except* blue. Well, I'm not quite sure why, but it seems like everything's inversed for whatever reason when it gets spit out as commands for the LED. It just works. <sub>little lies, stunning shows...</sup>
Full code's [here](https://github.com/rmiller85/CircuitPython/blob/master/rgb.py).

## Hello VS Code
This was my first introduction to VS Code. Basic stuff, just printing "Hello there!" every second. I also made it print `General Kenobi! You are a bold one...` in response, because I'm a big heckin nerd. Code's at [hello_vs_code.py](https://github.com/rmiller85/CircuitPython/blob/master/hello_vs_code.py).

## FancyLED
Back 
