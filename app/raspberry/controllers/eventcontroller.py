from gpiozero import Button, LED
from signal import pause


led = LED(pin=17)
button = Button(pin=19)


def initialize():
    button.when_pressed = led.on
    button.when_released = led.off


pause()


