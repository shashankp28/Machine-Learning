from pynput import keyboard
import time


key_press_times = {}


def on_press(key):
    try:
        key_name = key.char
    except AttributeError:
        key_name = str(key)
    press_time = time.time()
    print(f"Key {key_name} pressed at {press_time}")
    key_press_times[key_name] = press_time

def on_release(key):
    print(f"{key} released")
    if key == keyboard.Key.esc:
        return False

with open("keylog.txt", "w") as f:
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

    # At this point, you could do something with the collected key press times
    # For example, printing the dictionary
    print(key_press_times)
