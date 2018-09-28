from pypom import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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

        def click_my_account(self):
            self.find_element(*self._my_account_locator).click()

        def click_login(self):
            self.find_element(*self._login_locator).click()

        def click_logout(self):
            self.find_element(*self._logout_locator).click()

    class Header(Page):
        _search_box_locator = (By.CSS_SELECTOR, "#search > input")
        _cart_locator = (By.CSS_SELECTOR, "#cart > button")

        @property
        def is_search_box_present(self):
            return self.is_element_present(*self._search_box_locator)

        def search_for(self, search_term):
            search_field = self.find_element(*self._search_box_locator)
            search_field.send_keys(search_term)
            search_field.send_keys(Keys.RETURN)
            from frontend.pages.search import Search
            return Search(self.driver, self.base_url).wait_for_page_to_load()

        # todo: continue to adapt methods

    class Footer(Page):
        pass

