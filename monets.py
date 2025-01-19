import time
import uiautomator2 as u2
from datetime import datetime as dt

##########
#0  x 1080
#
#y 2060

class  UI:

    def xx(self, x):
        return x

    def yy(self, y):
     return y

    def Init(self):
        self.d = u2.connect()
        print(self.d.info)
        self.width, self.height = self.d.window_size()

    def pe(self,xp="//android.widget.TextView"):
        for elem in self.d.xpath(xp).all():
            print("Text:", elem.text)
            print("Attrib:", elem.attrib)
            print("Position:", elem.center())

    def ss(self, fn=""):
        self.d.screenshot(dt.now().strftime("%Y-%m-%d_%H_%M") +  fn + ".jpg")

    def xml(self, fn=""):
        with open(dt.now().strftime("%Y-%m-%d_%H_%M") +  fn + ".xml", 'w') as f:
           s = self.d.dump_hierarchy()
           f.write(s)

    def wait(salf, sec=10):
        time.sleep(sec)

    def GetAli(self):
        #self.d.app_stop_all()
        self.d.app_stop("ru.aliexpress.buyer")
        app = self.d.session("ru.aliexpress.buyer")
        self.wait(2)
        if self.d(textContains='Профиль').exists(timeout=30) is True:
           self.ss("A1")
           self.d(textContains='Профиль').click()
           self.wait(2)
           if self.d(textContains='Чаты').exists(timeout=30) is True:
               self.ss("A2")
               self.d.swipe(1000, 1500, 1000, 0)
               self.wait(2)
           try:
              self.ss("A3")
              self.d.xpath('//*[@resource-id="DisneylandBanner"]').click()
              self.wait(2)
              if self.d(textContains='День 1').exists(timeout=30) is True:
                  self.ss("A4")
                  if self.d(textContains='Монеты собраны!').exists(timeout=30) is False:
                    self.d.click(self.d(textContains='День 1').center()[0],
                                 self.d(textContains='День 1').center()[1] + 360)
                    self.wait(5)
                    self.ss("AX")
                  else:
                    self.ss("A0")
           except:
               self.d.app_stop("ru.aliexpress.buyer")
               self.ss("AE1")
        else:
           self.ss("AE2")
        self.wait(3)
        self.d.app_stop("ru.aliexpress.buyer")

    def GetYan(self):

        self.d.app_stop("ru.beru.android")
        app = self.d.session("ru.beru.android")
        self.wait(20)
        self.xml("Y0")

        if self.d(textContains='Пункт выдачи').exists(timeout=30) is True:
           self.ss("Y1")
           e=self.d(textContains='Пункт выдачи')
           self.xml("Y1")
           ui.d.click( e.center()[0]+500, e.center()[1] )
           self.wait(2)
           self.ss("Y2")
           self.xml("Y2")
           ui.d.click(860, 160)
           self.wait(2)
           self.ss("Y3")
           self.xml("Y3")
           ui.d.click(500, 1900)
           self.wait(2)
           self.ss("Y4")
           self.xml("Y4")
        else:
           print("Пункт выдачи не найдено")
           self.ss("YE")
        self.d.app_stop("ru.beru.android")

if __name__ == "__main__":
    ui = UI()
    ui.Init()
    ui.GetAli()
    ui.GetYan()

