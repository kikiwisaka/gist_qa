import os
from time import sleep
import unittest
from appium import webdriver
from helper import screen
from helper import custom_logger

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

logger = custom_logger.LoggerHelper().json_logger()

class TestShopee(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'Generic Test'
        desired_caps['noReset'] = True
        desired_caps['appActivity'] = "com.shopee.app.ui.home.HomeActivity_"
        desired_caps['startActivity'] = "com.shopee.app.ui.home.StartupActivity"
        desired_caps['app'] = PATH(
            './app_collection/ShopeeID.apk'
        )

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_1_login(self):
        logger.info("{0}".format('================='))
        logger.info("{0}".format('test_1_login'))
        logger.info("{0}".format('================='))
        sleep(4)

        if screen.Screen(self.driver, 'xpath', '//android.widget.TextView[@text="Beranda"]').wait_until_element_visible():
            self.driver.find_element('xpath', '//android.widget.TextView[@text="Saya"]').click()
            logger.debug('Tab Saya opened')
            if screen.Screen(self.driver, 'xpath', '//android.widget.Button[@text="Log In"]').wait_until_element_visible():
                self.driver.find_element('xpath', '//android.widget.Button[@text="Log In"]').click()
                print('Log In clicked')
                if screen.Screen(self.driver, 'xpath', '//android.widget.Button[@text="LOG IN"]').wait_until_element_visible():
                    email = self.driver.find_element('xpath', '//android.widget.EditText[@text="Email/Telepon/Username"]')
                    if email:
                        email.send_keys('kwisaka@bbmtek.com')
                        sleep(2)
                        pwd = self.driver.find_element('xpath', '//android.widget.EditText[@text="Password"]')
                        if pwd:
                            pwd.send_keys('Passw0rd')
                            sleep(2)
                            self.driver.find_element('xpath', '//android.widget.Button[@text="LOG IN"]').click()
                            logger.info("{0}".format('--------------------------------------'))
                            logger.info('Login success')
                            assert True
            else:
                print('locator not found')
                assert False
        else:
            print('beranda not found')
            assert False

    def test_2_add_item_to_chart(self):
        logger.info("{0}".format('================='))
        logger.info("{0}".format('test_2_add_item_to_chat'))
        logger.info("{0}".format('================='))
        sleep(4)

        if screen.Screen(self.driver, 'xpath', '//android.widget.TextView[@text="Elektronik Center"]').wait_until_element_visible():
            self.driver.find_element('xpath', '//android.widget.TextView[@text="Elektronik Center"]').click()
            if screen.Screen(self.driver, 'xpath', '//android.widget.TextView[@text="Cari dalam Elektronik Center | 15 Feb-14 Mar"]').wait_until_element_visible():
                self.driver.find_element('xpath', '//android.widget.TextView[@text="Cari dalam Elektronik Center | 15 Feb-14 Mar"]').click()
                sleep(2)
                keyword = self.driver.find_element('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout')
                if keyword:
                    keyword.send_keys('power bank')

                sleep(1)
                self.driver.find_element('xpath', '//android.widget.TextView[@text="powerbank"]').click()
                logger.info('Open keyword')
                sleep(3)
                logger.info('Choosing item')
                self.driver.find_element('xpath', '//android.view.ViewGroup[@instance="35"]').click()
                sleep(2)
                self.driver.find_element('xpath', '//android.widget.TextView[@text="Beli Sekarang"]').click()
                sleep(2)

                if screen.Screen(self.driver, 'xpath', '//android.widget.TextView[@text="Keranjang Saya"]').wait_until_element_visible():
                    screen.Context(self.driver).change_to_webview()
                    print('webview')
                    sleep(2)
                    self.driver.find_element("xpath", "//div[contains(@class, 'check-out clickable_area')]").click()
                    sleep(2)
                    if screen.Screen(self.driver, 'xpath', '//android.widget.TextView[@text="Checkout"]').wait_until_element_visible():
                        logger.info("{0}".format('--------------------------------------'))
                        logger.info('Add to chart SUCCESS')
                        assert True


        else:
            logger.info("{0}".format('--------------------------------------'))
            logger.warn('Add to chart FAILED')
            assert False

    def test_3_edit_chart(self):
        logger.info("{0}".format('================='))
        logger.info("{0}".format('test_3_edit_chat'))
        logger.info("{0}".format('================='))
        sleep(4)

        if screen.Screen(self.driver, 'xpath', '//android.widget.TextView[@text="Beranda"]').wait_until_element_visible():
            self.driver.find_element('xpath', '//android.widget.TextView[@text="Saya"]').click()
            logger.debug('Tab Saya opened')
            self.driver.find_element('xpath', '//android.widget.RelativeLayout[@instance="5"]').click()
            sleep(2)

            if screen.Screen(self.driver, 'xpath', '//android.widget.TextView[@text="Keranjang Saya"]').wait_until_element_visible():
                screen.Context(self.driver).change_to_webview()
                sleep(2)
                self.driver.find_element("xpath", "//div[contains(@class, 'ic_number_reduce clickable_area')]").click()
                sleep(2)
                if screen.Screen(self.driver, "xpath", "//div[contains(@class, 'check-out clickable_area')]").wait_until_element_visible():
                    self.driver.find_element("xpath", "//div[contains(@class, 'check-out clickable_area')]").click()
                    logger.info("{0}".format('--------------------------------------'))
                    logger.info('Edit chart SUCCESS')
                    assert True
        else:
            logger.info("{0}".format('--------------------------------------'))
            logger.info('Edit chart FAILED')
            assert False


    def test_4_delete_chart(self):
        logger.info("{0}".format('================='))
        logger.info("{0}".format('test_4_delete_chart'))
        logger.info("{0}".format('================='))
        sleep(4)

        if screen.Screen(self.driver, 'xpath', '//android.widget.TextView[@text="Beranda"]').wait_until_element_visible():
            self.driver.find_element('xpath', '//android.widget.TextView[@text="Saya"]').click()
            logger.debug('Tab Saya opened')
            sleep(3)
            self.driver.find_element('xpath', '//android.widget.RelativeLayout[@instance="5"]').click()
            sleep(3)

            if screen.Screen(self.driver, 'xpath', '//android.widget.TextView[@text="Keranjang Saya"]').wait_until_element_visible():
                screen.Context(self.driver).change_to_webview()
                sleep(2)
                self.driver.find_element("xpath", "//div[contains(@class, 'shop-edit-button edit m14 clickable_area')]").click()
                sleep(3)

                if screen.Screen(self.driver, "xpath", "//span[contains(@class, 'capitalize r14 pannel-delete__label')]").wait_until_element_visible():
                    self.driver.find_element("xpath", "//span[contains(@class, 'capitalize r14 pannel-delete__label')]").click()
                    screen.Context(self.driver).change_to_native()
                    sleep(3)
                    self.driver.find_element('xpath', '//android.widget.TextView[@text="HAPUS"]').click()
                    logger.info("{0}".format('--------------------------------------'))
                    logger.info('Delete chart SUCCESS')
                    assert True
        else:
            logger.info("{0}".format('--------------------------------------'))
            logger.info('Delete chart FAILED')
            assert False