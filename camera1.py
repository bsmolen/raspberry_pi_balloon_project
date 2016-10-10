#Revision: 0.01 (10/9/16) Author: B. Smolen
#Powers an LED off of GPIO 12 for 5 seconds then depowers
#Starts camera for 10 seconds then stops camera
from picamera import PiCamera
from gpiozero import LED, Button
from time import sleep
camera = PiCamera()
led = LED(12)
led.on()
camera.start_preview()
sleep(10)
led.off()
camera.stop_preview()
