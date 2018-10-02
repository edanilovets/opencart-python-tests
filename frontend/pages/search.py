from pypom import Region
from selenium.webdriver.common.by import By

from frontend.pages.base import Base


class Search(Base):

    _result_locator = (By.CSS_SELECTOR, '#content div.product-thumb')
    _showing_pages_locator = (By.CSS_SELECTOR, '#content > div:nth-child(9) > div.col-sm-6.text-right')
    _no_results_locator = (By.CSS_SELECTOR, '#content > p:nth-child(7)')

    def wait_for_page_to_load(self):
        self.wait.until(lambda _: self.find_element(By.CSS_SELECTOR, '#content'))
        return self

    @property
    def results_count(self):
        return len(self.find_elements(*self._result_locator))

    @property
    def search_results(self):
        return [self.SearchResult(self, el) for el in self.find_elements(*self._result_locator)]

    @property
    def number_of_pages(self):
        element = self.find_element(*self._showing_pages_locator)
        return element.get_attribute('innerText')[-8:-7]

    @property
    def no_results_message(self):
        return self.find_element(*self._no_results_locator).text

    class SearchResult(Region):

        _product_page_link_locator = (By.CSS_SELECTOR, 'h4 a')
        _product_name_locator = (By.CSS_SELECTOR, 'h4')
        # _product_add_to_cart_locator = (By.CSS_SELECTOR, 'button:nth-child(1)')

        def __repr__(self):
            return self.name

        def open_product_page(self):
            self.find_element(*self._product_page_link_locator).click()
            from frontend.pages.product import Product
            return Product(self.page.driver, self.page.base_url).wait_for_page_to_load()

        @property
        def name(self):
            return self.find_element(*self._product_name_locator).text
