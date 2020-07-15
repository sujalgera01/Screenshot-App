import time
import pyautogui

def screenshot():
    name = int(round(time.time()*1000))
    name = "C:/Users/sujal/Desktop/codes/Screenshot-App/images/{}.png".format(name)
    time.sleep(7)
    img = pyautogui.screenshot(name)
    img.show()

for i in range(0,5):
    screenshot()