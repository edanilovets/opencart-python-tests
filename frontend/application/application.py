from selenium import webdriver


class Application:

    def __init__(self, browser):
        if browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--start-maximized")
            # chrome_options.add_argument("--headless")
            self.wd = webdriver.Chrome(chrome_options=chrome_options)
        elif browser == "firefox":
            # using custom profile to start Firefox with
            # firefox_profile = webdriver.FirefoxProfile(
            # "C:\\Users\\Evgeniy Danilovets\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\p0dfg3xg.custom_profile1")
            # firefox_options = webdriver.FirefoxOptions()
            # firefox_options.add_argument("--devtools")
            # firefox_options.add_argument("--headless")
            # binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
            # self.wd = webdriver.Firefox(firefox_binary=binary,
            #                             options=firefox_options, firefox_profile=firefox_profile)
            # self.wd = webdriver.Firefox(firefox_binary=binary)
            self.wd = webdriver.Remote("http://localhost:4444/wd/hub",
                                       desired_capabilities={"browserName": "firefox", "platform": "LINUX"})
        elif browser == "edge":
            self.wd = webdriver.Edge()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser {}".format(browser))

    @property
    def driver(self):
        return self.wd

    def destroy(self):
        self.wd.quit()
