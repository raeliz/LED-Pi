from led_api.app import app
import RPi.GPIO as GPIO



if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    app.run(debug=True, port=80, host='0.0.0.0')
