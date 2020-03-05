from gpiozero import LED, PingServer
from gpiozero.tools import negated
from signal import pause

<<<<<<< HEAD
green = LED(5)
red = LED(5)
=======
green = LED(4)
red = LED(6)
>>>>>>> c994cca9b1bf6ba0218d3a1b248c4630953c7c0d

google = PingServer('google.com')

green.source = google
green.source_delay = 20
red.source = negated(green)

pause()