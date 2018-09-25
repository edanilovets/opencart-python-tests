class LoginPage:
    def __init__(self, app, selectors):
        self.app = app
        self.selectors = selectors

    def input_email(self):
        wd = self.app.wd
        selectors = self.selectors
        return wd.find_element_by_xpath(selectors['login']['input_email'])

    def input_password(self):
        wd = self.app.wd
        selectors = self.selectors
        return wd.find_element_by_xpath(selectors['login']['input_password'])

    def btn_login(self):
        wd = self.app.wd
        selectors = self.selectors
        return wd.find_element_by_xpath(selectors['login']['btn_login'])