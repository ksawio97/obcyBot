import pyautogui as pg
import keyboard as keyb
import time

class ActionController():
    run = True
    
    def locatingKeyObjects():
        captchaFound = not pg.locateOnScreen("captcha.png") == None
        
        if captchaFound:
            ActionController.run = False
            print("captcha!")
            return
        toSkip = "skip3.png"  
        skip = pg.locateOnScreen(toSkip)

        if not skip == None:
            print("skipped")
            pg.press("esc")
            time.sleep(2)

    def clickOnTypeArea(self):
        toSkip = "rozłaczSie.png"
        button = pg.locateOnScreen(toSkip)
        if not button == None:
            pg.click(button[0] + 200, button[1])
            print("found")
        else:
            print("didnt found")
        return not button == None

    def repeatMessageAllertHandle():
        button = pg.locateOnScreen("powtarzaSie.PNG")
        if not button == None:
            pg.click(button[0], button[1])
        

    def writeMessage(text, waitTime = 2):
        pg.write(text)
        time.sleep(waitTime)    
        pg.press('enter')
        ActionController.repeatMessageAllertHandle()


    def skipPerson():    
        pg.press('esc')
        time.sleep(0.2)
        pg.press('esc')