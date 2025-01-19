import time
import uiautomator2 as u2
import logging
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

    def pe(self):
        for elem in self.d.xpath("//android.widget.TextView").all():
            print("Text:", elem.text)
            print("Attrib:", elem.attrib)
            print("Position:", elem.center())

    def wait(salf, sec=10):
        time.sleep(sec)

    def test_simple(self):
        self.d = u2.connect()
        print(self.d.info)
        self.width, self.height = self.d.window_size()

        self.d.app_stop_all()
        app = self.d.session("ru.aliexpress.buyer")
        #self.wait(10)
        #print( self.d.app_current() )

        if self.d(textContains='Профиль').exists(timeout=30) is True:
           self.d.screenshot(dt.now().strftime("%Y-%m-%d_%H_%M")+"A.jpg")
           self.d(textContains='Профиль').click()
           self.wait(2)
           if self.d(textContains='Чаты').exists(timeout=30) is True:
              self.d.swipe(1000, 1500, 1000, 0)
           try:
              self.d.xpath('//*[@resource-id="DisneylandBanner"]').click()
              self.wait(5)
           except:
              print("ex1")
        else:
           print("<Профиль> не найдена")
           self.d.screenshot(dt.now().strftime("%Y-%m-%d_%H_%M")+"PNF.jpg")

        # self.d(textContains='+2').click()
        if self.d(textContains='День 1').exists(timeout=30) is True:
          ui.d.click(ui.d(textContains='День 1').center()[0], ui.d(textContains='День 1').center()[1] + 100)
          self.wait(2)
          ui.d.click(ui.d(textContains='День 2').center()[0], ui.d(textContains='День 2').center()[1] + 100)
          self.wait(2)
          ui.d.click(ui.d(textContains='День 3').center()[0], ui.d(textContains='День 3').center()[1] + 100)
          self.wait(2)
          ui.d.click(ui.d(textContains='День 4').center()[0], ui.d(textContains='День 4').center()[1] + 100)
          self.wait(2)
          ui.d.click(ui.d(textContains='День 5').center()[0], ui.d(textContains='День 5').center()[1] + 100)
          self.wait(2)
          ui.d.click(ui.d(textContains='День 6').center()[0], ui.d(textContains='День 6').center()[1] + 100)
          self.wait(10)
        self.d.app_stop_all()

if __name__ == "__main__":
#    logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    ui = UI()
    ui.test_simple()

