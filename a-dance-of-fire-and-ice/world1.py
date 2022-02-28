from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

degree_180 = 0.397
degree_270 = 0.6
degree_90 = 0.187

time.sleep(3)
print("** start game **")

# press space and release
def press_space():
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    print("space bar pressed")

press_space() # start game
time.sleep(2.35) # start delay
press_space()

for i in range(30):
    time.sleep(degree_180) # 180 degree delay
    press_space()

time.sleep(degree_270) # 270 degree delay
press_space()

time.sleep(degree_90) # 90 degree delay
press_space()

for i in range(14):
    time.sleep(degree_180) # 180 degree delay
    press_space()

time.sleep(degree_270) # 270 degree delay
press_space()

time.sleep(degree_90) # 90 degree delay
press_space()

for i in range(14):
    time.sleep(degree_180) # 180 degree delay
    press_space()

time.sleep(degree_270) # 270 degree delay
press_space()

time.sleep(degree_90) # 90 degree delay
press_space()

for i in range(14):
    time.sleep(degree_180) # 180 degree delay
    press_space()

time.sleep(degree_90) # 90 degree delay
press_space()

time.sleep(degree_270) # 270 degree delay
press_space()

for i in range(14):
    time.sleep(degree_180) # 180 degree delay
    press_space()

time.sleep(degree_90) # 90 degree delay
press_space()

time.sleep(degree_270) # 270 degree delay
press_space()

for i in range(12):
    time.sleep(degree_180) # 180 degree delay
    press_space()

time.sleep(degree_90) # 90 degree delay
press_space()

time.sleep(degree_270) # 270 degree delay
press_space()

time.sleep(degree_90) # 90 degree delay
press_space()

time.sleep(degree_270) # 270 degree delay
press_space()

for i in range(8):
    time.sleep(degree_180) # 180 degree delay
    press_space()

time.sleep(degree_270) # 270 degree delay
press_space()

time.sleep(degree_90) # 90 degree delay
press_space()

time.sleep(degree_270) # 270 degree delay
press_space()

time.sleep(degree_90) # 90 degree delay
press_space()

time.sleep(degree_270) # 270 degree delay
press_space()

time.sleep(degree_90) # 90 degree delay
press_space()

time.sleep(degree_270) # 270 degree delay
press_space()

time.sleep(degree_90) # 90 degree delay
press_space()

for i in range(12):
    time.sleep(degree_180) # 180 degree delay
    press_space()

time.sleep(degree_90) # 90 degree delay
press_space()

time.sleep(degree_270) # 270 degree delay
press_space()

time.sleep(degree_90) # 90 degree delay
press_space()

time.sleep(degree_270) # 270 degree delay
press_space()

for i in range(8):
    time.sleep(degree_180) # 180 degree delay
    press_space()

time.sleep(degree_270) # 270 degree delay
press_space()

time.sleep(degree_90) # 90 degree delay
press_space()

time.sleep(degree_270) # 270 degree delay
press_space()

time.sleep(degree_90) # 90 degree delay
press_space()

for i in range(2):
    time.sleep(degree_180) # 180 degree delay
    press_space()

time.sleep(degree_90) # 90 degree delay
press_space()

time.sleep(degree_270) # 270 degree delay
press_space()

for i in range(6):
    time.sleep(1.555) # 180 degree delay
    press_space()