from selenium import webdriver


class LoginDetails(object):
    driver = object

    def __init__(self, driver):
        self.driver = driver

    def get_userName(self):
        return self.driver.find_element_by_id("username")

    def get_password(self):
        return self.driver.find_element_by_id("password")

    def get_login_button(self):
        return self.driver.find_element_by_name("login")