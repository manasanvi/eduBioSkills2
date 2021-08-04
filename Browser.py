from selenium import webdriver


def createDriver(exeDriver):
    driver = webdriver.Chrome(executable_path=exeDriver)
    return driver


def openChrome():
    exeDriver = r"C:\Users\manas\Drivers\chromeDriverZip_v91\chromedriver_win32\chromedriver.exe"
    driver = createDriver(exeDriver)
    driver.get(r"https://www.edubioskills.com/")
    print(driver.title)
    print(driver.current_url)
    print(driver.current_window_handle)

    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


if __name__ == '__main__':
    openChrome()