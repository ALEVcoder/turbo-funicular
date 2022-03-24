# python -m pip install pyautogui

import pyautogui as pg
import time

print('5 sekunddan kiyin yozish uchun joyni tanlang')
time.sleep(5)

for i in range(100):
    pg.write("Xabar")
    time.sleep(0.5)
    print("Ketmoqda....")
    print("Ketdi")
    pg.press("Enter")
   