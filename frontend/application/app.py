from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/opencart/")

    def check_exists_by_link_text(self, link_text):
        wd = self.wd
        try:
            wd.find_element_by_link_text(link_text)
        except NoSuchElementException:
            return False
        return True

    def create_customer(self, customer, subscribe):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_xpath("//div[@id='top-links']/ul/li[2]/a").click()

        if self.check_exists_by_link_text("Register"):
            wd.find_element_by_link_text("Register").click()
        elif self.check_exists_by_link_text("Logout"):
            wd.find_element_by_link_text("Logout").click()
            wd.find_element_by_xpath("//div[@id='top-links']/ul/li[2]/a").click()
            wd.find_element_by_link_text("Register").click()
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
            wd.find_element_by_css_selector("input[name=newsletter]").click()

        wd.find_element_by_name("agree").click()
        wd.find_element_by_css_selector("input.btn.btn-primary").click()

    def destroy(self):
        self.wd.quit()
