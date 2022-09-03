from fastapi import FastAPI
from pydantic import BaseModel
from gpiozero import LED

app = FastAPI()

in_meeting = False

led_pin = LED("GPIO21")

led_pin.off()

class NewState(BaseModel):
    new_state: bool


@app.get("/", status_code=200)
def read_root():
    global in_meeting
    
    return {"onair": in_meeting, "led_state": led.value}


@app.post("/")
def set_meeting_state(new_state: NewState):
    global in_meeting
    in_meeting = new_state.new_state

    if in_meeting:
        led.on()
    else:
        led.off()
    
    return {"onair": in_meeting}
