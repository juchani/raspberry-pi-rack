from gpiozero import LED
from time import sleep as t 

<<<<<<< HEAD:1.py
led = LED(4)
=======
led = LED(6)
>>>>>>> c994cca9b1bf6ba0218d3a1b248c4630953c7c0d:34444.py

while 1:
    print(led.is_lit)
    led.on()
    t(10)
    print(led.is_lit)
    led.off()
    t(10)
