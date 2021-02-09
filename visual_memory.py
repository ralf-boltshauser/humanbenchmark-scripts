import pyautogui
import win32api
import win32gui
from time import sleep
import keyboard
import time


class coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


stop = False

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
tiles = []

stepSize = 80
level = 0

while (not stop):
    if (level > 3):
        stepSize = 70
    elif (level > 7):
        stepSize = 20
    elif (level > 21):
        stepSize = 10
    screenshot = pyautogui.screenshot(region=(50, 265, 938 - 100, 700 - 295))
    width, height = screenshot.size
    
    screenshot.save("./vm.png")
    for x in range(stepSize, width, stepSize):
        for y in range(stepSize, height, stepSize):
            r,g,b = screenshot.getpixel((x, y))
            if (255 == r and 255 == g and 255 == b):
                startTime = time.time()
                tile = coordinate(x + 50,y + 265)
                print(len(tiles))                
                if (not any(tile.x == tileLoop.x and tile.y == tileLoop.y for tileLoop in tiles)):
                    print(len(tiles))
                    tiles.append(tile)
    if len(tiles) > 0 and time.time() - startTime > 2: 
        print("press")
        for i in tiles:
            print("Clicking (" + str(i.x) + ":" + str(i.y) +")")
            pyautogui.click(i.x, i.y)
        level += 1
        tiles = []
        sleep(1)
    if (keyboard.is_pressed("s")):
        print(rgbint2rgbtuple(pyautogui.position().x, pyautogui.position().y))
    if (keyboard.is_pressed("q")):
        stop = True
