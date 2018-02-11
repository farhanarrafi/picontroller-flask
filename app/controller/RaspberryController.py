from gpiozero import Button, LED
from signal import pause


class RaspberryController:

    led = LED(pin=17)
    button = Button(pin=19)

    def __init__(self):
        self.led = LED(pin=17)
        self.button = Button(pin=19)
        self.button.when_pressed = self.led.on
        self.button.when_released = self.led.off


    def turnOn(self, pin):
        self.led = LED(pin=pin)
        self.led.on()


    def turnOff(self, pin):
        self.led = LED(pin=pin)
        self.led.off()

