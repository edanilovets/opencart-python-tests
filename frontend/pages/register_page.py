from selenium.common.exceptions import NoSuchElementException


class RegisterPage:
    def __init__(self, app, selectors):
        self.app = app
        self.selectors = selectors

    def first_name(self):
        wd = self.app.wd
        return wd.find_element_by_name("firstname")

    def first_name_warning(self):
        wd = self.app.wd
        try:
            return wd.find_element_by_css_selector("#account > div:nth-child(3) > div > div")
        except NoSuchElementException:
            print("No such element '{}' in DOM".format("#account > div:nth-child(3) > div > div"))

    def is_first_name_warning(self):
        return True if self.first_name_warning() else False

    def last_name(self):
        wd = self.app.wd
        return wd.find_element_by_name("lastname")

    def last_name_warning(self):
        wd = self.app.wd
        selectors = self.selectors
        return wd.find_element_by_xpath(selectors['account']['warning_lastname'])

    def email(self):
        wd = self.app.wd
        return wd.find_element_by_name("email")

    def email_warning(self):
        wd = self.app.wd
        selectors = self.selectors
        return wd.find_element_by_xpath(selectors['account']['warning_email'])

    def telephone(self):
        wd = self.app.wd
        return wd.find_element_by_name("telephone")

    def telephone_warning(self):
        wd = self.app.wd
        selectors = self.selectors
        return wd.find_element_by_xpath(selectors['account']['warning_phone'])

    def password(self):
        wd = self.app.wd
        return wd.find_element_by_name("password")

    def password_warning(self):
        wd = self.app.wd
        selectors = self.selectors
        return wd.find_element_by_xpath(selectors['account']['warning_password'])

    def confirm(self):
        wd = self.app.wd
        return wd.find_element_by_name("confirm")

    def confirm_warning(self):
        wd = self.app.wd
        selectors = self.selectors
        return wd.find_element_by_xpath(selectors['account']['warning_confirm'])

    def subscribe_yes(self):
        wd = self.app.wd
        selectors = self.selectors
        return wd.find_element_by_xpath(selectors['account']['subscribe_yes'])

    def checkbox_agree(self):
        wd = self.app.wd
        selectors = self.selectors
        return wd.find_element_by_xpath(selectors['account']['checkbox_agree'])

    def btn_continue(self):
        wd = self.app.wd
        selectors = self.selectors
        return wd.find_element_by_xpath(selectors['account']['btn_continue'])


