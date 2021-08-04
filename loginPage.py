from selenium import webdriver
import unittest
import Browser
from loginLocators import LoginDetails as log_loc


class LoginTests(unittest.TestCase):

    def setUp(self):
        self.driver = Browser.openChrome()

    # 1.  With correct user name and login

    def test_login1(self, driver):

        user_name= log_loc.get_userName()
        password = log_loc.get_password()
        login_button = log_loc.get_login_button()

        print("User name Displayed:{0} and Enabled: {1}".format(user_name.is_displayed(), user_name.is_enabled()))
        # login_button = WebDriverWait(driver, 60).until(
        #     ec.visibility_of_element_located((By.CLASS_NAME, "account-container lightbox-inner")))
        user_name.send_keys("test1")
        password.send_keys("eduBio234$")
        login_button.click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
