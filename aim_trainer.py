import pyautogui
import keyboard

while not keyboard.is_pressed("q"):
    target = pyautogui.locateOnScreen("./target.png", confidence=0.5, region=(0,100,1000,800))
    if (target != None) :    
        pyautogui.click(target.left + target.width / 2, target.top + target.height / 2)