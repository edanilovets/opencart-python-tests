from selenium.webdriver.common.by import By

from frontend.pages.base import Base


class Register(Base):
    _first_name_locator = (By.ID, "input-firstname")
    _last_name_locator = (By.ID, "input-lastname")
    _email_locator = (By.ID, "input-email")
    _phone_locator = (By.ID, "input-telephone")
    _password_locator = (By.ID, "input-password")
    _confirm_locator = (By.ID, "input-confirm")
    _subscribe_yes_locator = (By.XPATH, "//*[@id='content']/form/fieldset[3]/div/div/label[1]/input")
    _private_policy_locator = (By.XPATH, "//*[@id='content']/form/div/div/input[1]")
    _continue_button_locator = (By.CSS_SELECTOR, "#content > form > div > div > input.btn.btn-primary")
    _alert_danger_locator = (By.CSS_SELECTOR, "#account-register > div.alert.alert-danger.alert-dismissible")

    def wait_for_page_to_load(self):
        self.wait.until(lambda _: self.find_element(By.CSS_SELECTOR, "#content"))
        return self

    def set_first_name(self, first_name):
        el = self.find_element(*self._first_name_locator)
        el.send_keys(first_name)

    def set_last_name(self, last_name):
        el = self.find_element(*self._last_name_locator)
        el.send_keys(last_name)

    def set_email(self, email):
        el = self.find_element(*self._email_locator)
        el.send_keys(email)

    def set_phone(self, phone):
        el = self.find_element(*self._phone_locator)
        el.send_keys(phone)

    def set_password(self, password):
        el = self.find_element(*self._password_locator)
        el.send_keys(password)

    def set_confirm(self, confirm):
        el = self.find_element(*self._confirm_locator)
        el.send_keys(confirm)

    def set_subscribe_yes(self):
        self.find_element(*self._subscribe_yes_locator).click()

    def check_private_policy(self):
        self.find_element(*self._private_policy_locator).click()

    def click_continue(self, leave_page=True):
        self.find_element(*self._continue_button_locator).click()
        if leave_page:
            from frontend.pages.accout_success import AccountSuccess
            return AccountSuccess(self.driver, self.base_url).wait_for_page_to_load()
        else:
            return self

    @property
    def alert_danger_message(self):
        return self.find_element(*self._alert_danger_locator).text
