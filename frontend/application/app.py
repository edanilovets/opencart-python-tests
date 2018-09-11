from selenium import webdriver


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/opencart/")

    def destroy(self):
        self.wd.quit()
