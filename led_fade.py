import time
import board
import pulseio

led = pulseio.PWMOut(board.D13, frequency=5000, duty_cycle=0) #sets the led pin, frequency, & duty cycle

while True:
    print("Starting!!")
    for i in range(100):
        if i < 50:
            led.duty_cycle = int(i * 2 * 65535 / 100) #brightens led & increases i
        else:
            led.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100) #dims led & decreases i
        time.sleep(.01)
    time.sleep(.1)
    print("we made it!")