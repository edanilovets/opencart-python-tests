from selenium.webdriver.common.by import By

from frontend.pages.base import Base


class Product(Base):
    _product_name_locator = (By.CSS_SELECTOR, "#content h1")
    _product_price_locator = (By.CSS_SELECTOR, "#content > div > div.col-sm-4 > ul:nth-child(4) > li:nth-child(1) > h2")
    _add_to_cart_button_locator = (By.CSS_SELECTOR, "#button-cart")

    @property
    def name(self):
        return self.find_element(*self._product_name_locator).text

    @property
    def price_string(self):
        return self.find_element(*self._product_price_locator).text

    def wait_for_page_to_load(self):
        self.wait.until(lambda _: self.find_element(By.CSS_SELECTOR, '#content'))
        return self

    def click_add_to_cart(self):
        self.find_element(*self._add_to_cart_button_locator).click()
