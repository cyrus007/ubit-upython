from microbit import *
import music

while True:
    """ default code has error decoding negative values
    music.pitch(accelerometer.get_y(), 10)
    """
    music.pitch(abs(accelerometer.get_y()), 10)