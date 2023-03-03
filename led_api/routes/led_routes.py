from led_api.app import app
import RPi.GPIO as GPIO
from flask import jsonify, request
from time import sleep
import json


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

    def state(self):
        GPIO.setup(self.pin, GPIO.IN)
        is_on = GPIO.input(self.pin)
        GPIO.setup(self.pin, GPIO.OUT)

        if is_on:
            return "on! :D"
        else:
            return "off! D:"


lights = {
    "red": Led(11, "red"),
    "blue": Led(13, "blue"),
    "white": Led(15, "white"),
    "green": Led(29, "green"),
    "yellow": Led(31, "yellow")
}


# helpers :)
def turn_all_on():
    for led in lights.values():
        led.on()


def turn_all_off():
    for led in lights.values():
        led.off()


# get all LEDs
@app.route('/leds')
def get_all_leds():
    # return "Hit the get all leds endpoint"
    leds = []

    for led in lights.values():
        res = {
            "color": led.color,
            "pin": led.pin,
            "state": led.state()
        }

        leds.append(res)

    return jsonify(leds)


# get LED detail
@app.route('/leds/<color>')
def get_led_detail(color):
    # return "Hit the led detail endpoint"
    led = lights.get(color)

    if led is None:
        return "color not found", 404

    res = {
        "color": led.color,
        "pin": led.pin,
        "state": led.state()
    }

    return jsonify(res)


# turn LEDs on
@app.route('/leds/<color>/on', methods=["GET", "PUT"])
def turn_leds_on(color):
    # return "Hit the turn on leds endpoint"
    # - find the light by the color
    led = lights.get(color)

    # - return error if color doesnt exist, 404
    if led is None:
        return "color not found", 404

    # - call the method to turn it on
    led.on()

    # - return a 200 , and message "light on"
    return "light on"


# turn LEDs off
@app.route('/leds/<color>/off', methods=["GET", "PUT"])
def turn_leds_off(color):
    # return "Hit the turn off leds endpoint"
    led = lights.get(color)

    if led is None:
        return "color not found", 404

    led.off()

    return "light off"


# create a lightshow!
@app.route('/leds/lightshow', methods=["GET", "PUT"])
def led_lightshow():
    # return "Hit the led lightshow endpoint"
    # define a length of time for dot, dash, and space
    # convert "hello world" into a time sequence (list of durations to sleep for)
    dot = 0.10
    dash = 0.30
    space = 0.70

    letter_to_morse_code = {
        "h": [dot, dot, dot, dot],
        "e": [dot],
        "l": [dot, dash, dot, dot],
        "o": [dash, dash, dash],
        " ": [space],
        "w": [dot, dash, dash],
        "r": [dot, dash, dot],
        "d": [dash, dot, dot]
    }

    phrase = "hello world"

    # make sure all lights are off before we begin
    turn_all_off()

    # loop through the letters in the phrase
    for letter in phrase:
        # look up the morse code translation using the letter as the key (this is a time sequence)
        sequence = letter_to_morse_code.get(letter)
        # turn on the lights, only for the amount of time specified by the current time sequence
        for time in sequence:
            turn_all_on()
            # only leave the light on for the amount of time required (sleep before turning it off)
            sleep(time)
            turn_all_off()
            sleep(time)
            # after everything is looped through, turn off all the lights
    turn_all_off()

    return "Thanks for watching! :D"


# bonus: user input morse code translator
@app.route('/leds/morsecode', methods=["GET", "POST"])
def led_morsecode():
    # return "Hit the morse code endpoint"
    dot = 0.10
    dash = 0.30
    space = 0.70

    morse_code_library = {
        " ": [space],
        "a": [dot, dash],
        "b": [dash, dot, dot, dot],
        "c": [dash, dot, dash, dot],
        "d": [dash, dot, dot],
        "e": [dot],
        "f": [dot, dot, dash, dot],
        "g": [dash, dash, dot],
        "h": [dot, dot, dot, dot],
        "i": [dot, dot],
        "j": [dot, dash, dash, dash],
        "k": [dash, dot, dash],
        "l": [dot, dash, dot, dot],
        "m": [dash, dash],
        "n": [dash, dot],
        "o": [dash, dash, dash],
        "p": [dot, dash, dash, dot],
        "q": [dash, dash, dot, dash],
        "r": [dot, dash, dot],
        "s": [dot, dot, dot],
        "t": [dash],
        "u": [dot, dot, dash],
        "v": [dot, dot, dot, dash],
        "w": [dot, dash, dash],
        "x": [dash, dot, dot, dash],
        "y": [dash, dot, dash, dash],
        "z": [dash, dash, dot, dot]
    }

    data = json.loads(request.data)

    phrase = data.get("message")

    turn_all_off()
    for letter in phrase:
        sequence = morse_code_library.get(letter)

        if sequence is None:
            return "please only letters"

        for time in sequence:
            turn_all_on()
            sleep(time)
            turn_all_off()
            sleep(time)
    turn_all_off()

    return f"Thanks for watching: '{phrase}' :D"
