from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(3)

# press space and release
def press_space():
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    print("space bar pressed")

press_space()
time.sleep(2.5)
press_space()