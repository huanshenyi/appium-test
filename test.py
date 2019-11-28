import uiautomator2 as u2
import time


class Handle_test(object):
    def __init__(self):
        self.d = u2.connect("127.0.0.1:62001")
        # self.d.app_start("jp.co.recruit.android.rikunabi.twenty")
        self.d.app_start("jp.mynavi.tenshoku.tenshoku")

    def get_size(self):
        size = self.d.window_size()
        time.sleep(5)
        self.d.app_clear("jp.mynavi.tenshoku.tenshoku")
        return size

    def click_login(self):
        self.d.xpath("//*[@resource-id='jp.co.recruit.android.rikunabi.twenty:id/home_login_button']").click()
        self.d.xpath("//*[@resource-id='jp.co.recruit.android.rikunabi.twenty:id/login_password_textinputlayout']/"
                     "android.widget.FrameLayout[1]").set_text("test")


if __name__ == "__main__":
    h = Handle_test()
    h.get_size()