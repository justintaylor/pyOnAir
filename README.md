# pyOnAir

Trigger an on air light (via GPIO) when DB flag is set




## work machine
1. Sends a REST POST request to the onair machine which is hosting a FastAPI and uvicorn api
    `https://onair.local:8000`
  sample body: `{"new_state": true}`

  - a GET to the same root path will return the current onair state

-----
`sudo apt install python3-rpi.gpio`

https://sourceforge.net/p/raspberry-gpio-python/wiki/install/

`export GPIOZERO_PIN_FACTORY=rpigpio`


## lights controller

#### FastAPI
##### for testing and development
Docker could be used if desired (FastAPI wouldn't run on my Windows machine)

- to make the API accessible on the network the host command has to be added
  `uvicorn main:app --reload --host 0.0.0.0`