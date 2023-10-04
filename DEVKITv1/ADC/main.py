# Complete project details at https://RandomNerdTutorials.com

#from machine import Pin, ADC
import machine
from time import sleep

pot = machine.ADC(machine.Pin(34))
pot.atten(machine.ADC.ATTN_11DB)       #Full range: 3.3v

potup = machine.Pin(4, machine.Pin.OUT)
potup.value(1)

toggle = 0

while True:
  pot_value = pot.read()
  #pot_value = pot.read_uv()
  print(pot_value)
  sleep(0.1)
  toggle= toggle+1
  if toggle > 10:
    toggle = 0
    potup.value(abs(potup.value()-1))
