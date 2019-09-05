import time
import board
import pulseio
from adafruit_motor import servo
import touchio

# create a PWMOut object on A2.
pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# sets the pins for the touch sensing wires
touch_A1 = touchio.TouchIn(board.A1)
touch_A0 = touchio.TouchIn(board.A0)

# Create a servo named serv.
serv = servo.Servo(pwm)

angle = 0


print("Here we go!")
while True:
    if touch_A0.value and angle < 180:
        print("Touched A0!")
        angle += 3
        serv.angle = angle
    elif touch_A1.value and angle > 0:
        angle -= 3
        print("Touched A1!")
        serv.angle = angle
    time.sleep(.05)
    print("Done")