class AccountPage:
    def __init__(self, app, selectors):
        self.app = app
        self.selectors = selectors

    def edit_account(self):
        wd = self.app.wd
        selectors = self.selectors
        return wd.find_element_by_xpath(selectors['account']['edit_account'])

    def edit_account_email(self):
        wd = self.app.wd
        selectors = self.selectors
        return wd.find_element_by_xpath(selectors['account']['edit_email'])

    def edit_account_firstname(self):
        wd = self.app.wd
        selectors = self.selectors
        return wd.find_element_by_xpath(selectors['account']['edit_firstname'])

    def edit_account_btn_continue(self):
        wd = self.app.wd
        selectors = self.selectors
        return wd.find_element_by_xpath(selectors['account']['edit_continue'])
