from gpiozero import LED
from time import sleep as t
led= LED(12)

while 1:
    led.off()
    t(2)
    led.on()
    t(2)