from ActionController import ActionController
import pyautogui as pg
x = 0
ac = ActionController()

while ac.run:
    ac.WriteMessage(f"test {x}")
    ac.LocatingKeyObjects()
    x += 1