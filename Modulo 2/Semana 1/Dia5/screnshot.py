import pyautogui
import time

# pyautogui.moveTo(1751,33)
# time.sleep(1)
# pyautogui.click()
# time.sleep(1)
# pyautogui.screenshot('exemplo2.png')

while True:
    pyautogui.screenshot(f"print_{time.time()}.png")
    time.sleep(3)