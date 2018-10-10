from pypom import Page, Region
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from frontend.model.product import ProductOverview


class Base(Page):

    @property
    def topline(self):
        return self.TopLine(self.driver, self.base_url)

    @property
    def header(self):
        return self.Header(self.driver, self.base_url)

    @property
    def footer(self):
        return self.Footer(self.driver, self.base_url)

    class TopLine(Page):
        _my_account_locator = (By.XPATH, "//div[@id='top-links']/ul/li[2]/a")
        _login_locator = (By.XPATH, "//div[@id='top-links']/ul/li[2]/ul/li[2]/a")
        _logout_locator = (By.XPATH, "//div[@id='top-links']/ul/li[2]/ul/li[5]/a")
        _register_locator = (By.XPATH, "//div[@id='top-links']/ul/li[2]/ul/li[1]/a")
        _my_account_dropdown_locator = (By.XPATH, "//div[@id='top-links']/ul/li[2]/ul/li[1]/a")

        @property
        def is_login_menu_item_present(self):
            return self.is_element_present(*self._login_locator)

        @property
        def is_logout_menu_item_present(self):
            return self.is_element_present(*self._logout_locator)

        # top line menu My Account
        def click_my_account(self):
            self.find_element(*self._my_account_locator).click()

        def click_register(self):
            self.find_element(*self._register_locator).click()
            from frontend.pages.register_page import Register
            return Register(self.driver, self.base_url).wait_for_page_to_load()

        def click_login(self):
            self.find_element(*self._login_locator).click()

        def click_my_account_dropdown(self):
            self.find_element(*self._my_account_dropdown_locator).click()

        def click_logout(self):
            self.find_element(*self._logout_locator).click()

    class Header(Page):
        _search_box_locator = (By.CSS_SELECTOR, "#search > input")
        _search_button_locator = (By.CSS_SELECTOR, '#search > span')
        _cart_locator = (By.CSS_SELECTOR, "#cart > button")
        _empty_cart_message_locator = (By.CSS_SELECTOR, "#cart > ul > li > p")
        _cart_result_locator = (By.CSS_SELECTOR, "#cart > ul > li:nth-child(1) > table > tbody > tr")
        _cart_popup_locator = (By.CSS_SELECTOR, "#cart > ul > li:nth-child(1) > table")

        @property
        def is_search_box_present(self):
            return self.is_element_present(*self._search_box_locator)

        def search_for(self, search_term):
            search_field = self.find_element(*self._search_box_locator)
            search_field.send_keys(search_term)
            search_field.send_keys(Keys.RETURN)
            from frontend.pages.search import Search
            return Search(self.driver, self.base_url).wait_for_page_to_load()

        @property
        def is_cart_present(self):
            return self.is_element_present(*self._cart_locator)

        @property
        def is_cart_popup_displayed(self):
            return self.is_element_displayed(*self._cart_popup_locator)

        @property
        def empty_cart_message(self):
            return self.find_element(*self._empty_cart_message_locator).text

        def click_on_cart(self):
            self.find_element(*self._cart_locator).click()
            self.wait.until(lambda s: self.find_elements(*self._cart_result_locator))

        # todo: continue to implement header methods
        def number_of_items_in_cart(self):
            pass

        def price_in_cart(self):
            pass

        @property
        def cart_results(self):
            return [self.CartResult(self, el) for el in self.find_elements(*self._cart_result_locator)]

        class CartResult(Region):
            _product_page_link_locator = (By.CSS_SELECTOR, "td.text-left > a")
            _product_qty_locator = (By.CSS_SELECTOR, "td:nth-child(3)")
            _product_price_locator = (By.CSS_SELECTOR, "td:nth-child(4)")
            _product_remove_button = (By.CSS_SELECTOR, "td:nth-child(5) > button")

            def open_product_page(self):
                self.find_element(*self._product_page_link_locator).click()
                from frontend.pages.product import Product
                return Product(self.page.driver, self.page.base_url).wait_for_page_to_load()

            def click_remove_button(self):
                self.find_element(*self._product_remove_button).click()

            @property
            def product(self):
                product_name = self.find_element(*self._product_page_link_locator).text
                qty_text = self.find_element(*self._product_qty_locator).text
                qty_text = qty_text.replace("x", "")
                qty_text = qty_text.replace(" ", "")
                product_qty = int(qty_text)
                product_price = self.find_element(*self._product_price_locator).text
                return ProductOverview(name=product_name, price=product_price, qty=product_qty)

        # todo: continue implement menu methods
        class MainMenu(Region):
            pass

    class Footer(Page):
        pass

