import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33, # type: ignore
    board.IO34, # type: ignore
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39

]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    volume = int((microphone.value - 15000) / 2730)

    print(volume)

    for i in range (0, volume):
        leds[i].value = True
    sleep(0.1)

    for i in range (0, volume):
        leds[i].value = False
    sleep(0.1)

    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?