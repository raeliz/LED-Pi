import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)

class Led(object):
    # constructor
    def __init__(self, pin, color):
        self.pin = pin
        self.color = color
        GPIO.setup(pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, 1)

    def off(self):
        GPIO.output(self.pin, 0)



# red = Led(11, "red")
# red.on()
# sleep(1)

leds = [
    Led(11, "red"),
    Led(13, "blue"),
    Led(15, "white"),
    Led(29, "green"),
    Led(31, "yellow")
]

for led in leds:
    print("Turning on: " + str(led.color))
    led.on()
    sleep(1)

for led in leds:
    print("Turning off: " + str(led.color))
    led.off()
    sleep(1)


GPIO.cleanup()