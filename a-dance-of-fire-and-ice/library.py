from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

# press space and release
def press_space():
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    print("space bar pressed")

# game start
def game_start(start_delay, speed=1):
    press_space() # start game
    time.sleep(start_delay * speed) # start delay
    press_space()

# up 90 degrees
def stair_up(degree_90, degree_270, speed=1):
    time.sleep(degree_90 * speed)
    press_space()

    time.sleep(degree_270 * speed)
    press_space()

# down 90 degrees
def stair_down(degree_270, degree_90, speed=1):
    time.sleep(degree_270 * speed)
    press_space()

    time.sleep(degree_90 * speed)
    press_space()

def basic_step(degree_180, speed=1):
    time.sleep(degree_180 * speed)
    press_space()