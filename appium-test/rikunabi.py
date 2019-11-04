__author__ = "ハリネズミ"
from appium import webdriver
import time

cap = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "jp.co.recruit.android.rikunabi.twenty",
  "appActivity": "jp.co.recruit.android.rikunabi.twenty.activity.home.HomeActivity",
  "noReset": True
}

# appiumに接続
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)

driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                             "FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4"
                             ".widget.DrawerLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager"
                             "/android.widget.RelativeLayout/android.view.View/android.widget.ScrollView/android.widget"
                             ".LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView").click()

time.sleep(2)

driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                             "FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4."
                             "widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android."
                             "support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.ScrollView/android"
                             ".widget.LinearLayout/android.widget.RelativeLayout/android.widget.EditText").send_keys("ベルフェイス")
time.sleep(1)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button[2]").click()



