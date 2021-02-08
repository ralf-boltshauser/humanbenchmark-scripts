import pyautogui
import keyboard
import json
from time import sleep

pic = pyautogui.screenshot(region=(0, 165, 938, 700 - 165))

width, height = pic.size
pic.save("./chip.png")
for x in range(0, width, 5):
    for y in range(0, height, 5):

        r, g, b = pic.getpixel((x, y))

        if r == 255 and g == 255 and b == 255:
            pic = pyautogui.screenshot(region=(x - 50, y + 100, 100, 100))
            pic.save("./chimp_screens/test" + str(x) + "." + str(y) + ".png")
            pyautogui.click(x + 50, y + 200)
            sleep(0.05)
            break

while not keyboard.is_pressed("q"):

    if keyboard.is_pressed("s"):
        print(pyautogui.position())
