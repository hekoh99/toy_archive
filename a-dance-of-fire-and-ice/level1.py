from pynput.keyboard import Key, Controller

keyboard = Controller()

# press space and release
keyboard.press(Key.space)
keyboard.release(Key.space)