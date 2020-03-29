import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


shutterpin = 17
solenoidpin = 27

GPIO.setup(shutterpin, GPIO.LOW)  

GPIO.setup(solenoidpin, GPIO.LOW)

#wiringpi.pinMode(shutterpin,1)

#wiringpi.pinMode(solenoidpin,1)

#GPIO.digitalWrite(solenoidpin,gpio.HIGH)

GPIO.output(solenoidpin, GPIO.HIGH)

sleep(0.06)

#gpio.digitalWrite(solenoidpin,gpio.LOW)

GPIO.output(solenoidpin, GPIO.LOW)

sleep(0.1)

GPIO.output(solenoidpin, GPIO.HIGH)

sleep(0.05)

GPIO.output(solenoidpin, GPIO.LOW)

sleep(0.12)

GPIO.output(shutterpin, GPIO.HIGH)

sleep(0.1)

GPIO.output(shutterpin, GPIO.LOW)