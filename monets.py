import time
import uiautomator2 as u2
import uiautomator2.image as u2image
#import cv2
#import numpy
from datetime import datetime as dt
import logging
import os

##########
#0  x 1080
#
#y 2060

logger = logging.getLogger(__name__)
logging.basicConfig(filename='monets.log', encoding='utf-8', level=logging.DEBUG)


class  UI:

    def Init(self):
        self.d = u2.connect()
        self.directory = dt.now().strftime("%Y-%m-%d")
        if not os.path.exists("./data/"+self.directory):
           os.makedirs("./data/"+self.directory)

    def log(self,s):
        self.ss(s)
        self.xml(s)
        logger.debug(s)

    def pe(self,xp="//android.widget.TextView"):
        for elem in self.d.xpath(xp).all():
            print("Text:", elem.text)
            print("Attrib:", elem.attrib)
            print("Position:", elem.center())

    def save_text(self,xp="//android.widget.TextView"):
        for elem in self.d.xpath(xp).all():
            fn = "./tmp/"+str(elem.bounds[0])+"_"+str(elem.bounds[1])+".png"
            elem.screenshot().save(fn)
            print(str(elem.bounds[0])+"_"+str(elem.bounds[1])+"_"+elem.text)

    def save_img(self,xp="//*[@bounds]"):
        for elem in self.d.xpath(xp).all():
            fn = "./tmp/"+str(elem.bounds[0])+"_"+str(elem.bounds[1])+".png"
            elem.screenshot().save(fn)
            print(str(elem.bounds[0])+","+str(elem.bounds[1])+"_"+elem.text)


    def ss(self, fn=""):
        self.d.screenshot("./data/"+self.directory+"/"+dt.now().strftime("%H_%M") +  fn + ".jpg")

    def xml(self, fn=""):
        with open("./data/"+self.directory+"/"+dt.now().strftime("%H_%M") +  fn + ".xml", 'w') as f:
           s = self.d.dump_hierarchy()
           f.write(s)

    def wait(salf, sec=10):
        time.sleep(sec)

    def wait_el(self, text="", time=10):
        t=time
        while t > 0 :
            print("t=",t," Text=", text)
            if self.d(textContains=text).exists(timeout=1) is True:
                self.el = self.d(textContains=text)
                return True
            t = t - 1
        return False

    def wait_xp(self, xp = "", timeout = 10):
        t = timeout
        deadline = time.time() + timeout
        while time.time() < deadline:
            e = self.d.xpath( xp )
            try:
                if  e.exists is True:
                    self.el = e
                    return True
            except:
                time.sleep(1)
            print(deadline - time.time() )
            t = t - 1
        return False

    def ImScr(self):
        #im = u2image.imread(filename)
        im = self.d.screenshot()
        u2image.show_image(im)
        #image = cv2.imread('./testim.jpg')
        #image = cv2.cvtColor(numpy.array(im), cv2.COLOR_RGB2BGR)
        #cv2.imshow('image window', image)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

    def ShowXP(self, xp = ""):
        self.el = self.d.xpath( xp )
        print(self.el.info)
        im = self.el.screenshot()
        u2image.show_image(im)

    def ShowEl(self ):
        print(self.el.info)
        im = self.el.screenshot()
        u2image.show_image(im)

    def LogE(self,fn="Err"):
        self.ss(fn)
        self.xml(fn)

    def GetAli(self):

        self.d.press("home")
        self.d.app_stop_all()
        # self.d.app_stop("ru.aliexpress.buyer")
        app = self.d.session("ru.aliexpress.buyer")
        self.log("A01")
        try:
            self.xp = "//*[@resource-id='ru.aliexpress.buyer:id/navigation_profile']/child::*[2]"
            if self.wait_xp(self.xp, 50) is False:
                self.LogE("AE1")
                return
            self.ce = self.d.xpath(self.xp)
            self.log("A03")
            self.ce.click()
            self.log("A04")

            self.xp = "//*[@text='Чаты']"
            if self.wait_xp(self.xp, 50) is False:
                self.LogE("AE2")
                return
            self.ce = self.d.xpath(self.xp)
            self.log("A05")
            self.d.swipe(1000, 1600, 1000, 100)

            self.xp = '//*[@resource-id="DisneylandBanner"]'
            if self.wait_xp(self.xp, 50) is False:
                self.LogE("AE3")
                return
            self.ce = self.d.xpath(self.xp)
            self.log("A06")
            self.ce.click()
            self.wait(10)

            #self.xp = '//*[@text="День 1"]'
            self.xp = '//*[@text="Собрать монеты"]'
            if self.wait_xp(self.xp, 50) is False:
                self.LogE("AE4")
                return
            self.ce = self.d.xpath(self.xp)
            self.log("A06")
            self.ce.click()
            self.wait(2)

        except:
            self.log("a-except")
            self.LogE("A_E")
        finally:
            self.log("a-finally")

    def GetYan(self):

        self.d.press("home")
        #self.d.app_stop("ru.beru.android")
        self.d.app_stop_all()
        app = self.d.session("ru.beru.android")
        self.log("Y01")

        try:
            self.xp = '//*[@content-desc="Монетки колеса призов"]/child::*[2]'
            if  self.wait_xp( self.xp , 50 ) is False:
                self.LogE("YE1")
                return
            self.ce = self.d.xpath( self.xp )
            self.log("Y02")
            self.ce.click()
            self.log("Y03")

            self.xp = '//*[@text="Заходите каждый день, чтобы собрать как можно больше монеток за неделю"]/ancestor::*[3]/child::*[2]/child::*[1]'
            if  self.wait_xp(self.xp) is True:
                self.log("Y04")
                self.ce = ui.d.xpath( self.xp )  # Надпись "Забрать награду"
                self.ce.click()
                self.log("Y05")
            else:
                self.xp = '//*[@text="Монетки за\xa0вход"]'
                if  self.wait_xp( self.xp ) is True:
                    self.log("Y06")
                    self.ce = self.d.xpath(self.xp)
                    self.log("Y07")
                    self.ce.click()
                    self.log("Y08")
                    ### Надпись "Забрать награду"
                    self.xp = '//*[@text="Заходите каждый день, чтобы собрать как\xa0можно больше монеток за неделю"]/ancestor::*[3]/child::*[2]/child::*[1]'
                    if  self.wait_xp( self.xp ) is True:
                        self.log("Y09")
                        self.ce = ui.d.xpath( self.xp )
                        self.ce.click()
                        self.log("Y10")
        except:
            self.LogE("YE1")
        finally:
            self.log("Y-finally")

if __name__ == "__main__":
    ui = UI()
    ui.Init()
    ui.d.screen_on()
    ui.d.app_stop_all()
    ui.GetAli()
    ui.d.screenshot("ali.jpg")
    ui.d.app_stop_all()
    ui.GetYan()
    ui.d.screenshot("yan.jpg")
    ui.d.app_stop_all()


