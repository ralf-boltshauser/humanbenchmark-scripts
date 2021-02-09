import pyautogui
import keyboard
import json
from time import sleep
from pytesseract import *


pic = pyautogui.screenshot(region=(0, 165, 938, 700 - 165))
width, height = pic.size

for x in range(0, width - 10, 5):
    for y in range(0, height - 10, 5):
        print(str(x) + ":" + str(y))
        r, g, b = pic.getpixel((x, y))
        if r == 255 and g == 255 and b == 255:
            pic = pyautogui.screenshot(region=(x - 100, y + 85, 200, 200))
            pic.save("./chimp_screens/test" + str(x) + "." + str(y) + ".png")
            pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'
            output = pytesseract.image_to_string(
                pic, config='--psm 7 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz')
            output = output.strip()
            if (len(output) > 0):
                print(output)
            pyautogui.click(x + 50, y + 200)
            sleep(0.05)
            break

while not keyboard.is_pressed("q"):

    if keyboard.is_pressed("s"):
        print(pyautogui.position())
