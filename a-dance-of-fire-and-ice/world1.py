import time
import library

degree_180 = 0.397
degree_270 = 0.6
degree_90 = 0.186
start_delay = 2.33

speed = 1

time.sleep(3)
print("** start game **")

library.game_start(start_delay)

for i in range(30):
    library.basic_step(degree_180)

library.stair_down(degree_270, degree_90)

for i in range(14):
    library.basic_step(degree_180)

library.stair_down(degree_270, degree_90)

for i in range(14):
    library.basic_step(degree_180)

library.stair_down(degree_270, degree_90)

for i in range(14):
    library.basic_step(degree_180)

library.stair_up(degree_90, degree_270)

for i in range(14):
    library.basic_step(degree_180)

library.stair_up(degree_90, degree_270)

for i in range(12):
    library.basic_step(degree_180)

for i in range(2):
    library.stair_up(degree_90, degree_270)

for i in range(8):
    library.basic_step(degree_180)

for i in range(4):
    library.stair_down(degree_270, degree_90)

for i in range(12):
    library.basic_step(degree_180)

for i in range(2):
    library.stair_up(degree_90, degree_270)

for i in range(8):
    library.basic_step(degree_180)

for i in range(2):
    library.stair_down(degree_270, degree_90)

for i in range(2):
    library.basic_step(degree_180)

library.stair_up(degree_90, degree_270)

for i in range(6):
    time.sleep(1.58) # snail
    library.press_space()