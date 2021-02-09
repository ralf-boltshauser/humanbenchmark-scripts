import pyautogui
import win32gui
from time import sleep
import keyboard

def rgbint2rgbtuple(x, y):
    RGBint = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), x, y)
    d = dict()
    d['b'] = RGBint & 255
    d['g'] = (RGBint >> 8) & 255
    d['r'] = (RGBint >> 16) & 255

    return d

stop = False
while (not stop):
    color = rgbint2rgbtuple(500, 500)
    if (color['r'] == 106 and color['g'] == 219 and color['b'] == 75):
        pyautogui.click(500, 500)
        sleep(0.5)
        pyautogui.click(500, 500)

    if (keyboard.is_pressed("q")):
        stop = True