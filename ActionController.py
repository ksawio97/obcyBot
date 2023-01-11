import pyautogui as pg
import time

class ActionController():

    def __init__(self):
        self.run = True
        self.sc = None
    
    def LoopActions(self):
        self.sc = pg.screenshot("screen.png")
        return self.run

    def FindOnScreen(self, img):
        return pg.locate(self, img)

    def LocatingKeyObjects(self):
        captchaFound = not self.FindOnScreen("images/captcha.png") == None
        
        if captchaFound:
            self.run = False
            print("captcha!")
            return
        toSkip = "images/skip3.png"  
        skip = self.FindOnScreen(toSkip)

        if not skip == None:
            print("skipped")
            pg.press("esc")
            time.sleep(2)

    def ClickOnTypeArea(self):
        toSkip = "images/rozłaczSie.png"
        button = self.FindOnScreen(toSkip)

        if not button == None:
            pg.click(button[0] + 200, button[1])

        return not button == None

    def RepeatMessageAllertHandle(self):
        button = self.FindOnScreen("images/powtarzaSie.PNG")
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