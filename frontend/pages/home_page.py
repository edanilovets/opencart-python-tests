class HomePage:
    def __init__(self, app, selectors):
        self.app = app
        self.selectors = selectors

    # def check_exists_by_xpath(self, xpath_selector):
    #     wd = self.wd
    #     try:
    #         wait = WebDriverWait(wd, 5)  # wait 5 seconds
    #         wait.until(EC.presence_of_element_located((By.XPATH, xpath_selector)))
    #     except TimeoutException:
    #         return False
    #     return True

    def open(self):
        wd = self.app.wd
        wd.get("http://localhost:8080/opencart/")

    def topline_my_account(self):
        wd = self.app.wd
        selectors = self.selectors
        return wd.find_element_by_xpath(selectors['top_line']['my_account'])

    def topline_account(self):
        wd = self.app.wd
        selectors = self.selectors
        return wd.find_element_by_xpath(selectors['top_line']['account'])

    def topline_register(self):
        wd = self.app.wd
        selectors = self.selectors
        return wd.find_element_by_xpath(selectors['top_line']['register'])

    def topline_login(self):
        wd = self.app.wd
        selectors = self.selectors
        return wd.find_element_by_xpath(selectors['top_line']['login'])

    def topline_logout(self):
        wd = self.app.wd
        selectors = self.selectors
        return wd.find_element_by_xpath(selectors['top_line']['logout'])
