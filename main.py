import pyautogui as pg
import keyboard as keyb
from ActionController import ActionController
import time



# def holdKey(key, seconds):
#     startTime = time.time()
#     while time.time() < startTime + seconds:
#         pg.press(key)
controller = ActionController()

while controller.run:
    print("looking")
    controller.locatingKeyObjects()
    # if keyb.is_pressed('a'):
    #     print("worked!")
    #     controller.skipPerson()
    