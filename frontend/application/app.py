from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from frontend.application.login_page import LoginPage
from frontend.application.register_page import RegisterPage


class Application:

    def __init__(self, config, browser):
        if browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--start-maximized")
            # chrome_options.add_argument("--headless")
            self.wd = webdriver.Chrome(chrome_options=chrome_options)
        elif browser == "firefox":
            # using custom profile to start Firefox with
            firefox_profile = webdriver.FirefoxProfile(
                "C:\\Users\\Evgeniy Danilovets\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\p0dfg3xg.custom_profile1")
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("--devtools")
            # firefox_options.add_argument("--headless")
            binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
            self.wd = webdriver.Firefox(firefox_binary=binary, options=firefox_options, firefox_profile=firefox_profile)
        elif browser == "edge":
            self.wd = webdriver.Edge()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser {}".format(browser))

        self.config = config

        # self.login = LoginPage(self)
        # self.register = RegisterPage(self)

    def maximize_window(self):
        wd = self.wd
        wd.maximize_window()

    def check_exists_by_xpath(self, xpath_selector):
        wd = self.wd
        try:
            wd.find_element_by_xpath(xpath_selector)
        except NoSuchElementException:
            return False
        return True

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/opencart/")

    def open_login_page(self):
        wd = self.wd
        xpath = self.config
        wd.find_element_by_xpath(xpath['top_line']['my_account']).click()
        if self.check_exists_by_xpath(xpath['top_line']['login']) and \
                wd.find_element_by_xpath(xpath['top_line']['login']).text == "Login":
            wd.find_element_by_xpath(xpath['top_line']['login']).click()
        else:
            raise NoSuchElementException("Cannot find <Login> link. Check your UI.")

    def open_register_page(self):
        wd = self.wd
        xpath = self.config
        wd.find_element_by_xpath(xpath['top_line']['my_account']).click()

        if self.check_exists_by_xpath(xpath['top_line']['register']) and \
                wd.find_element_by_xpath(xpath['top_line']['register']).text == "Register":
            wd.find_element_by_xpath(xpath['top_line']['register']).click()
        else:
            raise NoSuchElementException("Cannot find <Register> link. Check you UI.")

    def login(self, customer):
        wd = self.wd
        xpath = self.config
        self.open_home_page()
        self.open_login_page()
        wd.find_element_by_xpath(xpath['login']['input_email']).send_keys(customer.email)
        wd.find_element_by_xpath(xpath['login']['input_password']).send_keys(customer.password)
        wd.find_element_by_xpath(xpath['login']['btn_login']).click()

    def is_customer_logged_in(self, customer):
        wd = self.wd
        xpath = self.config
        wd.find_element_by_xpath(xpath['top_line']['my_account']).click()
        if self.check_exists_by_xpath(xpath['top_line']['account']) and \
                wd.find_element_by_xpath(xpath['top_line']['account']).text == "My Account":
            wd.find_element_by_xpath(xpath['top_line']['account']).click()
            wd.find_element_by_xpath(xpath['account']['edit_account']).click()
            email = wd.find_element_by_xpath(xpath['account']['edit_email']).get_attribute("value")
            if email == customer.email:
                return True
            else:
                return False
        else:
            return False

    def logout(self):
        wd = self.wd
        xpath = self.config
        self.open_home_page()
        wd.find_element_by_xpath(xpath['top_line']['my_account']).click()
        if self.check_exists_by_xpath(xpath['top_line']['logout']) and \
                wd.find_element_by_xpath(xpath['top_line']['logout']).text == "Logout":
            wd.find_element_by_xpath(xpath['top_line']['logout']).click()
        else:
            raise NoSuchElementException("You are not logged in.")

    def create_customer(self, customer, subscribe=False):
        wd = self.wd
        xpath = self.config
        self.open_home_page()
        self.open_register_page()

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

    def edit_customer_firstname(self, customer):
        wd = self.wd
        xpath = self.config
        wd.find_element_by_xpath(xpath['top_line']['my_account']).click()
        wd.find_element_by_xpath(xpath['top_line']['account']).click()
        wd.find_element_by_xpath(xpath['account']['edit_account']).click()
        wd.find_element_by_xpath(xpath['account']['edit_firstname']).clear()
        wd.find_element_by_xpath(xpath['account']['edit_firstname']).send_keys(customer.firstname)
        wd.find_element_by_xpath(xpath['account']['edit_continue']).click()

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

    def is_login_warning_message_showed(self):
        wd = self.wd
        xpath = self.config
        warning = wd.find_element_by_xpath(xpath['login']['warning']).get_attribute("innerText")
        if warning == " Warning: No match for E-Mail Address and/or Password.":
            return True
        else:
            return False

    def destroy(self):
        self.wd.quit()
