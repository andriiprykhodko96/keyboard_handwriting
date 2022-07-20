from pynput.keyboard import Listener
from time import time

start = 0

def measure_times(times):
    def on_press(key):
        global start
        if start == 0:
            start = time()

    def on_release(key):
        global start
        times.append(time() - start)
        start = 0
        if len(times) == 10:
            return False

    with Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()

    return times
