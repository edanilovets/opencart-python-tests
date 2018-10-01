from selenium.webdriver.common.by import By

from frontend.pages.base import Base


class Product(Base):
    _product_name_locator = (By.CSS_SELECTOR, "#content h1")
    _add_to_cart_button_locator = (By.CSS_SELECTOR, "#button-cart")

    @property
    def name(self):
        return self.find_element(*self._product_name_locator).text

    def wait_for_page_to_load(self):
        self.wait.until(lambda _: self.find_element(By.CSS_SELECTOR, '#content'))
        return self

    def click_add_to_cart(self):
        self.find_element(*self._add_to_cart_button_locator).click()
