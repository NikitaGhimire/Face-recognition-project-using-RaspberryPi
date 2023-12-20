import subprocess
import sys
import os
import gpiozero
from gpiozero import LED
from gpiozero import OutputDevice
from gpiozero import MotionSensor
from time import sleep
 
motion_sensor= MotionSensor(27)
green_led = LED(17)
red_led = LED(18)
relay_pin=26
relay=gpiozero.OutputDevice(relay_pin,active_high=True, initial_value=False)

def doorlock():
    returned_text = subprocess.check_output(
        "python3 email_notification``.py", shell=True, universal_newlines=True)
    print(returned_text)
    if "Hello" in returned_text:
        print("Door is Open")
        green_led.on()
        relay.on()
        sleep(10)
        print("Door is closed")
        green_led.off()
        relay.off()
        sleep(10)
    else:
        print("unknown user")
        red_led.on()
        sleep(10)
        red_led.off()
        sleep(10)

while True:
    if motion_sensor.wait_for_motion():
        print("Motion detected")
        doorlock()
        
