from selenium.webdriver.common.by import By

from frontend.pages.base import Base


class AccountSuccess(Base):
    URL_TEMPLATE = '/index.php?route=account/success'
    _congratulation_message_locator = (By.CSS_SELECTOR, "#content > p:nth-child(2)")

    def wait_for_page_to_load(self):
        self.wait.until(lambda _: self.find_element(By.CSS_SELECTOR, '#content'))
        return self

    @property
    def is_congratulation_message_present(self):
        return self.is_element_present(*self._congratulation_message_locator)

    @property
    def congratulation_message(self):
        return self.find_element(*self._congratulation_message_locator).text
