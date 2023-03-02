import RPi.GPIO as GPIO
from time import sleep



GPIO.setmode(GPIO.BOARD)

red = 11
blue = 13
white = 15
green = 29
yellow = 31

leds = [ red, blue, white, green, yellow ]

for led in leds:
    GPIO.setup(led, GPIO.OUT)

# GPIO.setup(red, GPIO.OUT)
# GPIO.setup(blue, GPIO.OUT)
# GPIO.setup(white, GPIO.OUT)
# GPIO.setup(green, GPIO.OUT)
# GPIO.setup(yellow, GPIO.OUT)

for blinks in range(5):

    for led in leds:
        GPIO.output(led, 1)
        sleep(0.2)

    backwards = leds.copy()
    backwards.reverse()
    for led in backwards:
        GPIO.output(led, 0)
        sleep(0.2)

        
    # 1 = GPIO.HIGH // 0 = GPIO.LOW

    # GPIO.output(red, 1)
    # sleep(0.2)
    # GPIO.output(blue, 1)
    # sleep(0.2)
    # GPIO.output(white, 1)
    # sleep(0.2)
    # GPIO.output(green, 1)
    # sleep(0.2)
    # GPIO.output(yellow, 1)
    # sleep(0.2)

    # GPIO.output(red, 0)
    # sleep(0.2)
    # GPIO.output(blue, 0)
    # sleep(0.2)
    # GPIO.output(white, 0)
    # sleep(0.2)
    # GPIO.output(green, 0)
    # sleep(0.2)
    # GPIO.output(yellow, 0)
    # sleep(0.2)
    



# turns lights off / resets ...
GPIO.cleanup()