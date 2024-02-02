import pyautogui
import time
from pynput import keyboard

# Coordinates
x, y = 100, 100   # First point
x2, y2 = 200, 200 # Second point

exit_program = False

def on_press(key):
    global exit_program
    if key == keyboard.Key.esc:
        exit_program = True
        return False  # Stop the listener

listener = keyboard.Listener(on_press=on_press)
listener.start()

try:
    while not exit_program:
        pyautogui.moveTo(x, y)
        time.sleep(1)
        pyautogui.moveTo(x2, y2)
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    listener.stop()
