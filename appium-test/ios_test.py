from appium import webdriver
import time

capability = {
      "automationName": "XCUITest",
      "platformName": "iOS",
      "platformVersion": "13.2",
      "deviceName": "iPhone Simulator",
      "app": ".appのpath",
      "noReset": "true"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capability)
# 自動アラートを閉じる(ios特有)
driver.switch_to.alert.accept()

# 左へswipe(公式推奨解決方法)
driver.execute_script("mobile:scroll", {"direction": "right"})

# iosだけの関数
driver.find_element_by_ios_predicate("type=='XCUIElementTypeTestField' ADN value=='何か'").send_keys("123")
time.sleep(1)

driver.quit()


# モニターサイズを取得
def get_size():
    width = driver.get_window_size()["width"]
    height = driver.get_window_size()["height"]
    return width, height


# 左へswipe
def swipe_left():
    x1 = get_size()[0]/10*9
    y1 = get_size()[1]/2
    x = get_size()[0]/10
    driver.swipe(x1, y1, x, y1, 2000)


# 下へswipe
def swipe_down():
    x1 = get_size()[0]/2
    y1 = get_size()[1]/10
    y = get_size()[1]/10*9
    driver.swipe(x1, y1, x1, y)


def swipe_on(direction):
    if direction == "up":
        pass
    if direction == "down":
        swipe_down()
    if direction == "left":
        swipe_left()
    else:
        pass



