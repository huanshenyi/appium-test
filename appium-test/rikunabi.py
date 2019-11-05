__author__ = "ハリネズミ"
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# cap = {
#   "platformName": "Android",
#   "platformVersion": "5.1.1",
#   "deviceName": "127.0.0.1:62001",
#   "appPackage": "jp.co.recruit.android.rikunabi.twenty",
#   "appActivity": "jp.co.recruit.android.rikunabi.twenty.activity.home.HomeActivity",
#   "noReset": True
# }

# appiumに接続
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)


class Rikunabi(object):
    def __init__(self):
        self.cap = {
                      "platformName": "Android",
                      "platformVersion": "5.1.1",
                      "deviceName": "127.0.0.1:62001",
                      "appPackage": "jp.co.recruit.android.rikunabi.twenty",
                      "appActivity": "jp.co.recruit.android.rikunabi.twenty.activity.home.HomeActivity",
                      "noReset": True
                    }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.cap)

    def do_this(self):
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                                     "FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4"
                                     ".widget.DrawerLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager"
                                     "/android.widget.RelativeLayout/android.view.View/android.widget.ScrollView/android.widget"
                                     ".LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView").click()
        locator = (By.XPATH,
                                   "/hierarchy/android.widget.FrameLayout/android."
                                   "widget.LinearLayout/android.widget."
                                   "FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support."
                                   "v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout"
                                   "/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget."
                                   "ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget"
                                   ".EditText")

        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(locator))

        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                             "FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4."
                             "widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android."
                             "support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.ScrollView/android"
                             ".widget.LinearLayout/android.widget.RelativeLayout/android.widget.EditText").send_keys("リクルート")
        time.sleep(1)
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button[2]").click()
        l = self.get_size()
        # 最初の位置
        x1 = int(l[0]*0.5)
        # どこからスクロール
        y1 = int(l[1]*0.75)
        # 何処で止まる
        y2 = int(l[1]*0.25)
        time.sleep(2)
        # スクロール操作
        while True:
            self.driver.swipe(x1, y1, x1, y2)
            time.sleep(0.5)

    # スクロール用
    def get_size(self):
        x = self.driver.get_window_size()["width"]
        y = self.driver.get_window_size()["height"]
        return (x, y)


if __name__ == "__main__":
    r = Rikunabi()
    r.do_this()


