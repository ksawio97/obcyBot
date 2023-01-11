import pyautogui as pg
import time

class ActionController():

    def __init__(self):
        self.run = True

    def Loop(self):
        self.LocatingKeyObjects()
        self.ClickOnTypeArea()

        return self.run

    def LocatingKeyObjects(self):
        captchaFound = not pg.locateOnScreen("images/captcha.png") == None
        
        if captchaFound:
            self.run = False
            print("captcha!")
            return
        toSkip = "images/skip3.png"  
        skip = pg.locateOnScreen(toSkip)

        if not skip == None:
            print("skipped")
            pg.press("esc")
            time.sleep(2)

    def ClickOnTypeArea(self):
        startCoord = "images/rozłaczSie.png"
        button = pg.locateOnScreen(startCoord)

        if not button == None:
            pg.click(button[0] + 200, button[1])

        return not button == None

    def RepeatMessageAllertHandle(self):
        button = pg.locateOnScreen("images/powtarzaSie.PNG")
        if not button == None:
            pg.click(button[0], button[1])

    def WriteMessage(self, text, waitTime = 2):
        pg.write(text)
        time.sleep(waitTime)    
        pg.press('enter')
        self.RepeatMessageAllertHandle()


    def SkipPerson():    
        pg.press('esc')
        time.sleep(0.2)
        pg.press('esc')