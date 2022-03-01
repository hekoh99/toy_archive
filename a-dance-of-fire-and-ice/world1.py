from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

degree_180 = 0.397
degree_270 = 0.6
degree_90 = 0.186

time.sleep(3)
print("** start game **")

# press space and release
def press_space():
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    print("space bar pressed")

# game start
def game_start():
    press_space() # start game
    time.sleep(2.35) # start delay
    press_space()

# up 90 degrees
def stair_up():
    time.sleep(degree_90)
    press_space()

    time.sleep(degree_270)
    press_space()

# down 90 degrees
def stair_down():
    time.sleep(degree_270)
    press_space()

    time.sleep(degree_90)
    press_space()

game_start()

for i in range(30):
    time.sleep(degree_180) # 180 degrees delay
    press_space()

stair_down()

for i in range(14):
    time.sleep(degree_180)
    press_space()

stair_down()

for i in range(14):
    time.sleep(degree_180)
    press_space()

stair_down()

for i in range(14):
    time.sleep(degree_180)
    press_space()

stair_up()

for i in range(14):
    time.sleep(degree_180)
    press_space()

stair_up()

for i in range(12):
    time.sleep(degree_180)
    press_space()

for i in range(2):
    stair_up()

for i in range(8):
    time.sleep(degree_180)
    press_space()

for i in range(4):
    stair_down()

for i in range(12):
    time.sleep(degree_180)
    press_space()

for i in range(2):
    stair_up()

for i in range(8):
    time.sleep(degree_180)
    press_space()

for i in range(2):
    stair_down()

for i in range(2):
    time.sleep(degree_180)
    press_space()

stair_up()

for i in range(6):
    time.sleep(1.557) # snail
    press_space()