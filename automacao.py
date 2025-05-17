import pyautogui
import time

count = 1

pyautogui.hotkey("win", "e")

time.sleep(1)

pyautogui.hotkey("win", "down")

time.sleep(2)

while count <= 5:
	pyautogui.press("tab")
	count = count + 1