from numpy.core import numeric
import pyautogui
import keyboard
from PIL import Image
from pytesseract import *
import win32gui
from time import sleep
import numpy as np
import cv2
from pytesseract import image_to_string
import matplotlib.pyplot as plt
import json

def rgbint2rgbtuple(x, y):
    RGBint = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), x, y)
    d = dict()
    d['b'] = RGBint & 255
    d['g'] = (RGBint >> 8) & 255
    d['r'] = (RGBint >> 16) & 255

    return d

numbers = []
while not keyboard.is_pressed("q"):
    if (rgbint2rgbtuple(467,546)['r'] == 84):
        print("Typing")
        for number in numbers:
            sleep(0.1)
            keyboard.press(str(number))
        sleep(0.5)
        keyboard.press('enter')
        sleep(1)
        keyboard.press('enter')
    else: 
        print("Reading")
        img = pyautogui.screenshot(region=(0,375,900,100))
        img.save("./number.png")
        #plt.imshow(img)
        #plt.show()
        pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'
        output = pytesseract.image_to_string(img, config='--psm 7 -c tessedit_char_whitelist=0123456789')

        if (len(output) > 0):
            numbers = []
            numbers = [int(s) for s in [char for char in output] if s.isdigit()];

        if (len(numbers) > 0):
            print(numbers)
            sleep(1)


        
        