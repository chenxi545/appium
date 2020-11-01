from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy



class TestWokrWeiXin:
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            # caps["settings[waitForIdleTimeout]"] = 0
            "noReset": True,  # 不重置APP
            "skipServerInstallation": True,  # 跳过 uiAutomator2服务器安装
            "dontStopAppOnReset": True,
            "skipDeviceInitialization": True,  # 跳过设备初始化
            "unicodeKeyboard": True,  # 默认启用 Unicode 输入
            "resetKeyboard": True, # 与上面合用，可以输入中文
            "appWaitDuration": 60000
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_wechart_daka(self):
        sleep(10)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="工作台"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("打卡").instance(0));').click()
        self.driver.update_settings({"waitForIdleTimeout": 0})
        sleep(5)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hiy").click()
        sleep(10)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '次外出')]").click()
        sleep(3)
        assert "外出打卡成功" in self.driver.page_source




