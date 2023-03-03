## LED-Pi

> Hiya! This is just a fun little project to practice Python and Flask. Welcome to my first API :)

### API Endpoints:

* `GET/leds` - gets all leds connected. Returns all LEDs in JSON format: 
  ```json
  [
      {
          "color": "green",
          "pin": 29,
          "state": "off"
      }
  ]
  ```


* `GET/leds/:color` - gets the specified LED by color. Returns single LED in JSON format for `/leds/blue`:
  ```json
  [
      {
          "color": "blue",
          "pin": 13,
          "state": "on"
      }
  ]
  ```
  

* `PUT/leds/:color/on` - turns on the light specified (this will also update the "state" value for the `GET/leds` endpoint and the `GET/leds/:color` endpoint to `"state": "on"`)

* `PUT/leds/:color/off` - turns off the light specified (this will also update the "state" value for the `GET/leds` endpoint and the `GET/leds/:color` endpoint to `"state": "off"`)

* `PUT/leds/lightshow` - flashes the LEDs to "hello world" in morse code

* `POST/leds/morsecode` - uses a morse code library to translate request message to a flashing morse code response (try it yourself!)






https://user-images.githubusercontent.com/111096348/222811486-5aad9158-bfe7-48d4-83ce-2ee1dc13fdb8.mov

