from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from frontend.pages.account_page import AccountPage
from frontend.pages.home_page_old import HomePage
from frontend.pages.login_page import LoginPage
from frontend.pages.main_menu_block import MainMenu
from frontend.pages.register_page import RegisterPage


class Application:

    def __init__(self, selectors, browser):
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

        self.wait = WebDriverWait(self.wd, 10)
        self.selectors = selectors
        self.main_menu_block = MainMenu(self)
        self.home_page = HomePage(self, selectors)
        self.login_page = LoginPage(self, selectors)
        self.register_page = RegisterPage(self, selectors)
        self.account_page = AccountPage(self, selectors)

    def save_screen_shot(self):
        wd = self.wd
        wd.save_screenshot("screen.png")

    def maximize_window(self):
        wd = self.wd
        wd.maximize_window()

    def login(self, customer):
        self.home_page.topline_my_account().click()
        self.home_page.topline_login().click()

        self.login_page.input_email().send_keys(customer.email)
        self.login_page.input_password().send_keys(customer.password)
        self.login_page.btn_login().click()

    def is_customer_logged_in(self, customer):
        self.home_page.topline_my_account().click()
        self.home_page.topline_account().click()

        self.account_page.edit_account().click()
        if self.account_page.edit_account_email().get_attribute("value") == customer.email:
            return True
        else:
            return False

    def logout(self):
        self.home_page.topline_my_account().click()
        self.home_page.topline_logout().click()

    def create_customer(self, customer, subscribe=False):
        self.home_page.topline_my_account().click()
        self.home_page.topline_register().click()

        self.register_page.first_name().send_keys(customer.firstname)
        self.register_page.last_name().send_keys(customer.lastname)
        self.register_page.email().send_keys(customer.email)
        self.register_page.telephone().send_keys(customer.phone)
        self.register_page.password().send_keys(customer.password)
        self.register_page.confirm().send_keys(customer.password)

        if subscribe:
            self.register_page.subscribe_yes().click()

        self.register_page.checkbox_agree().click()
        self.register_page.btn_continue().click()

    def edit_customer_firstname(self, customer):
        self.home_page.topline_my_account().click()
        self.home_page.topline_account().click()

        self.account_page.edit_account().click()
        self.account_page.edit_account_firstname().clear()
        self.account_page.edit_account_firstname().send_keys(customer.firstname)
        self.account_page.edit_account_btn_continue().click()

    # todo: continue to transform code to page objects
    def get_content_headers(self):
        wd = self.wd
        content_headers = []
        current_window = wd.current_window_handle
        menu_elements = self.main_menu_block.list_of_menu_elements()
        for element in menu_elements:
            if element.get_attribute("class") == "dropdown":
                # todo: problem in locator with firefox
                inner_links = element.find_elements_by_tag_name("a")
                for inner_link in inner_links:
                    if inner_link.get_attribute("class") not in ["dropdown-toggle", "see-all"]:
                        ActionChains(wd).move_to_element(element).perform()
                        ActionChains(wd).move_to_element(inner_link).perform()
                        ActionChains(wd).key_down(Keys.CONTROL).click(inner_link).key_up(Keys.CONTROL).perform()
                        self.wait.until(EC.number_of_windows_to_be(2))
                        new_window = [window for window in wd.window_handles if window != current_window][0]
                        wd.switch_to.window(new_window)
                        header = self.wait.until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, "#content > h2:nth-child(1)")))
                        content_headers.append(header.text)
                        wd.close()
                        wd.switch_to.window(current_window)
            else:
                element = element.find_element_by_tag_name("a")
                ActionChains(wd).key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
                self.wait.until(EC.number_of_windows_to_be(2))
                new_window = [window for window in wd.window_handles if window != current_window][0]
                wd.switch_to.window(new_window)
                header = self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#content > h2:nth-child(1)")))
                content_headers.append(header.text)
                wd.close()
                wd.switch_to.window(current_window)
        return content_headers

    def destroy(self):
        self.wd.quit()
