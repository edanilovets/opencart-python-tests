class HomePage:
    def __init__(self, app, selectors):
        self.app = app
        self.selectors = selectors

    def open(self):
        wd = self.app.wd
        # wd.get("http://localhost:8080/opencart/")
        wd.get("https://demo.opencart.com")

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
