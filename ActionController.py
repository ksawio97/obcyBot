import pyautogui as pg
import keyboard as keyb
import threading
import time

class ActionController():
    def __init__(self):
        print("here")
        def leaveGate():
            while self.run: 
                if keyb.is_pressed('f1'):
                    run = False
                
        self.run = True
        
        leaveThread = threading.Thread(target=leaveGate, name="LeaveGate")
        # leaveThread.start()
    
    def locatingKeyObjects(self):
        captchaFound = not pg.locateOnScreen("captcha.png") == None
        
        if captchaFound:
            self.run = False
        for toSkip in ["skip3.png"]:  
            skip = pg.locateOnScreen(toSkip)
            if not skip == None:
                print("skipped")
                pg.click(skip[0], skip[1])
            else:
                print("didnt skip")
            
    def skipPerson():    
        pg.press('esc')
        time.sleep(0.2)
        pg.press('esc')