from ActionController import ActionController
import pyautogui as pg
x = 0
ac = ActionController()

while ac.Loop():
    ac.WriteMessage(f"test {x}")
    x += 1