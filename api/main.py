from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

in_meeting = False


class NewState(BaseModel):
    new_state: bool


@app.get("/", status_code=200)
def read_root():
    global in_meeting

    return {"onair": in_meeting}


@app.post("/")
def set_meeting_state(new_state: NewState):
    global in_meeting
    in_meeting = new_state.new_state

    return {"onair": in_meeting}
