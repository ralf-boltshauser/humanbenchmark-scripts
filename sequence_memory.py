import pyautogui
import win32api
import win32gui
from time import sleep
import keyboard
import time

class coordinate:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y


stop = False
buttonLocations = []

# Add coordinates of blocks
buttonLocations.append(coordinate(0, 340, 330))
buttonLocations.append(coordinate(1, 471, 330))
buttonLocations.append(coordinate(2, 604, 330))
buttonLocations.append(coordinate(3, 340, 450))
buttonLocations.append(coordinate(4, 471, 450))
buttonLocations.append(coordinate(5, 604, 450))
buttonLocations.append(coordinate(6, 340, 590))
buttonLocations.append(coordinate(7, 471, 590))
buttonLocations.append(coordinate(8, 604, 590))

order = ""
level = 0
def split(word): 
    return [char for char in word]  

def rgbint2rgbtuple(x, y):
    RGBint = win32gui.GetPixel(win32gui.GetDC(
        win32gui.GetActiveWindow()), x, y)
    d = dict()
    d['b'] = RGBint & 255
    d['g'] = (RGBint >> 8) & 255
    d['r'] = (RGBint >> 16) & 255

    return d

run = False
while (not run):
    if (keyboard.is_pressed("r")):
        run = True

startTime = time.time()
while (not stop):
    print(order)
    for i in buttonLocations:
        color = rgbint2rgbtuple(i.x, i.y)
        if (color['b'] == 255):
            startTime = time.time() 
            if (not order.endswith(str(i.id))):
                order = order + str(i.id)
    
    if (time.time() - startTime > 0.5):
        level += 1
        for i in split(order):
            for j in buttonLocations: 
                if (i == str(j.id)):
                    sleep(0.2)
                    print("Press on " + str(j.id))
                    pyautogui.click(j.x, j.y)
        order = ""
        

    if (keyboard.is_pressed("s")):
        print(rgbint2rgbtuple(pyautogui.position().x, pyautogui.position().y))
    if (keyboard.is_pressed("q")):
        stop = True