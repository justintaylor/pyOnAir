import time

from gpiozero import LED


in_meeting = False

led_pin = LED("GPIO21")

while True:
    led_pin.on()
    time.sleep(1)
    led_pin.off()
