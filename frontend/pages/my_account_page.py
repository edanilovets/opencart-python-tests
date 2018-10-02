from selenium.webdriver.common.by import By

from frontend.pages.base import Base


class MyAccount(Base):

    URL_TEMPLATE = '/index.php?route=account/account'

    def wait_for_page_to_load(self):
        self.wait.until(lambda _: self.find_element(By.CSS_SELECTOR, '#content'))
        return self


