import time
import _thread
from pynput.keyboard import Key, Listener
from bs4 import BeautifulSoup as bs
import os

html = open('/index.html')
soup = bs(html, 'html.parser')
old_text = soup.find("h1", {"class": "timcook"})
print(type(old_text))

t = float(input("Time never waits: "))
count = True
done = True
time_left = 0

def counting(t):
    global time_left
    global new_text
    global done

    while count is True and t != 0:
        time_left = t - 1
        t = time_left

        old_text.string.replace_with(str(t))

        with open("time.html", "wb") as f_output:
            f_output.write(soup.prettify("utf-8"))

        time.sleep(1)

    print("\a")
	
	
def on_press(key):
    global count
    try:
        if key.char == 'x':
            count = False
            print(f"Time left - {time_left}")
            time.sleep(1)
            count = True
            _thread.start_new_thread(counting, (t + time_left,))
    except:
        pass


with Listener(on_press=on_press) as listener:
    listener.join()

