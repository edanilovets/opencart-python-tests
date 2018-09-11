from selenium import webdriver


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/opencart/")

    def create_account(self):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_xpath("//div[@id='top-links']/ul/li[2]/a").click()
        wd.find_element_by_link_text("Register").click()

        def type_by_name(selector, text):
            wd.find_element_by_name(selector).click()
            wd.find_element_by_name(selector).clear()
            wd.find_element_by_name(selector).send_keys(text)

        type_by_name("firstname", "John")
        type_by_name("lastname", "Dilinger")
        type_by_name("email", "email1@mail.com")
        type_by_name("telephone", "+380978880088")
        type_by_name("password", "111111")
        type_by_name("confirm", "111111")

        wd.find_element_by_name("agree").click()
        wd.find_element_by_css_selector("input.btn.btn-primary").click()

    def destroy(self):
        self.wd.quit()
