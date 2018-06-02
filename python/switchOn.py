import RPi.GPIO as GPIO
import sys

pin = sys.argv[1]
mode = sys.argv[2]

if pin in ["21","11111","111122","11112223"]:
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  if mode == "on":
    print "on"
    GPIO.setup(int(pin), GPIO.OUT, initial=GPIO.HIGH)
  else:
    print "off"
    GPIO.setup(int(pin), GPIO.OUT, initial=GPIO.LOW)
else:
  print "pin not found"