import time
import library

degree_180 = 0.371
degree_270 = 0.565
degree_90 = 0.177
start_delay = 2.215

slow_180 = 1.484
s_to_r_180 = 0.769

def world2_pattern1():
    for i in range(3):
        library.basic_step(degree_180)

    library.basic_step(degree_270)

    for i in range(3):
        library.basic_step(degree_180)
    
    library.basic_step(degree_90)

def world2_pattern1_reverse():
    for i in range(3):
        library.basic_step(degree_180)
    
    library.basic_step(degree_90)

    for i in range(3):
        library.basic_step(degree_180)

    library.basic_step(degree_270)

time.sleep(3)
print("** game start **")

library.game_start(start_delay)

for i in range(3):
    world2_pattern1()

for i in range(4):
    library.basic_step(degree_180)

library.basic_step(degree_90)

for i in range(2):
    library.basic_step(degree_180)

library.basic_step(degree_270)

for i in range(3):
    world2_pattern1()

world2_pattern1_reverse()

for i in range(4):
    library.basic_step(slow_180)

for i in range(4):
    library.basic_step(s_to_r_180)

for i in range(8):
    library.basic_step(degree_180)

library.basic_step(degree_90)

for i in range(31):
    library.basic_step(degree_180)

library.basic_step(degree_90)

for i in range(3):
    world2_pattern1()

for i in range(4):
    library.basic_step(degree_180)

library.basic_step(degree_90)

for i in range(2):
    library.basic_step(degree_180)