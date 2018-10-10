from random import randrange

from frontend.pages.home_page import Home


class TestCart:
    def test_put_product_in_cart_from_search_output(self, app, base_url):
        home_page = Home(app.driver, base_url).open()
        search_page = home_page.header.search_for("apple")
        search_results = search_page.search_results
        pr_index = randrange(len(search_results))   # get random product index
        product_page = search_results[pr_index].open_product_page()
        product_page.click_add_to_cart()
        product_page.header.click_on_cart()
        assert product_page.name == product_page.header.cart_results[0].product.name
        assert product_page.price_string == product_page.header.cart_results[0].product.price

