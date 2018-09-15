from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class Application:

    def __init__(self, config):
        self.wd = webdriver.Chrome()
        self.config = config

    def maximize_window(self):
        wd = self.wd
        wd.maximize_window()

    def check_exists_by_link_text(self, link_text):
        wd = self.wd
        try:
            wd.find_element_by_link_text(link_text)
        except NoSuchElementException:
            return False
        return True

    def check_exists_by_xpath(self, xpath_selector):
        wd = self.wd
        try:
            wd.find_element_by_xpath(xpath_selector)
        except NoSuchElementException:
            return False
        return True

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/opencart/")

    def login(self, customer):
        wd = self.wd
        xpath = self.config
        self.open_home_page()
        wd.find_element_by_xpath(xpath['top_line']['my_account']).click()
        if self.check_exists_by_link_text("Login"):
            wd.find_element_by_xpath(xpath['top_line']['login']).click()
        elif self.check_exists_by_link_text("Logout"):
            wd.find_element_by_xpath(xpath['top_line']['logout']).click()
            wd.find_element_by_xpath(xpath['top_line']['my_account']).click()
            wd.find_element_by_xpath(xpath['top_line']['login']).click()
        else:
            raise NoSuchElementException("Cannot find Login/Logout links. Check your UI.")

        wd.find_element_by_xpath(xpath['login']['input_email']).send_keys(customer.email)
        wd.find_element_by_xpath(xpath['login']['input_password']).send_keys(customer.password)
        wd.find_element_by_xpath(xpath['login']['btn_login']).click()
        return True

    def logout(self):
        wd = self.wd
        xpath = self.config
        self.open_home_page()
        wd.find_element_by_xpath(xpath['top_line']['my_account']).click()
        if self.check_exists_by_link_text("Logout"):
            wd.find_element_by_xpath(xpath['top_line']['logout']).click()
        else:
            raise NoSuchElementException("You are not logged in.")

    def create_customer(self, customer, subscribe=False):
        wd = self.wd
        self.open_home_page()
        xpath = self.config

        wd.find_element_by_xpath(xpath['top_line']['my_account']).click()

        if self.check_exists_by_link_text("Register"):
            wd.find_element_by_xpath(xpath['top_line']['register']).click()
        elif self.check_exists_by_link_text("Logout"):
            wd.find_element_by_xpath(xpath['top_line']['logout']).click()
            wd.find_element_by_xpath(xpath['top_line']['my_account']).click()
            wd.find_element_by_xpath(xpath['top_line']['register']).click()
        else:
            raise NoSuchElementException("Cannot find Register/Logout links. Check you UI.")

        def type_by_name(selector, text):
            wd.find_element_by_name(selector).click()
            wd.find_element_by_name(selector).clear()
            wd.find_element_by_name(selector).send_keys(text)

        type_by_name("firstname", customer.firstname)
        type_by_name("lastname", customer.lastname)
        type_by_name("email", customer.email)
        type_by_name("telephone", customer.phone)
        type_by_name("password", customer.password)
        type_by_name("confirm", customer.password)

        if subscribe:
            wd.find_element_by_xpath(xpath['account']['subscribe_yes']).click()

        wd.find_element_by_xpath(xpath['account']['checkbox_agree']).click()
        wd.find_element_by_xpath(xpath['account']['btn_continue']).click()

    def is_warning_message_showed(self, field_name):
        wd = self.wd
        xpath = self.config
        if field_name == "Password":
            warn_message = wd.find_element_by_xpath(xpath['account']['warning_password']).text
            if warn_message == "Password must be between 4 and 20 characters!":
                return True
        elif field_name == "Password Confirm":
            warn_message = wd.find_element_by_xpath(xpath['account']['warning_confirm']).text
            if warn_message == "Password confirmation does not match password!":
                return True
        elif field_name == "First Name":
            warn_message = wd.find_element_by_xpath(xpath['account']['warning_firstname']).text
            if warn_message == "First Name must be between 1 and 32 characters!":
                return True
        elif field_name == "Last Name":
            warn_message = wd.find_element_by_xpath(xpath['account']['warning_lastname']).text
            if warn_message == "Last Name must be between 1 and 32 characters!":
                return True
        elif field_name == "E-mail":
            warn_message = wd.find_element_by_xpath(xpath['account']['warning_email']).text
            if warn_message == "E-Mail Address does not appear to be valid!":
                return True
        elif field_name == "Telephone":
            warn_message = wd.find_element_by_xpath(xpath['account']['warning_phone']).text
            if warn_message == "Telephone must be between 3 and 32 characters!":
                return True
        else:
            return False

    def destroy(self):
        self.wd.quit()
