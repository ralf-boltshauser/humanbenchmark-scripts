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
    RGBint = win32gui.GetPixel(win32gui.GetDC(
        win32gui.GetActiveWindow()), x, y)
    d = dict()
    d['b'] = RGBint & 255
    d['g'] = (RGBint >> 8) & 255
    d['r'] = (RGBint >> 16) & 255

    return d


seen = dict()
seen['x'] = 419
seen['y'] = 530


new = dict()
new['x'] = 545
new['y'] = 530
numbers = []

words = []

while not keyboard.is_pressed("q"):
    img = pyautogui.screenshot(region=(100, 375, 800, 100))
    img.save("./word.png")
    pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'
    output = pytesseract.image_to_string(
        img, config='--psm 7 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz')
    output = output.strip()
    if (len(output) > 0):
        print(output)
        if output not in words:
            pyautogui.click(new['x'], new['y'])
            words.append(output)
        else:
            pyautogui.click(seen['x'], seen['y'])

    if (keyboard.is_pressed("s")):
        print(pyautogui.position())

