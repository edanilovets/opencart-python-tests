from frontend.pages.home_page import Home
from random import randrange


class TestSearch:
    def test_search_results_are_shown(self, app, base_url):
        home_page = Home(app.driver, base_url).open()
        search_page = home_page.header.search_for("apple")
        assert search_page.results_count > 0

    def test_can_open_product_from_search_results(self, app, base_url):
        home_page = Home(app.driver, base_url).open()
        search_page = home_page.header.search_for("apple")
        search_results = search_page.search_results
        pr_index = randrange(len(search_results))   # get random product index
        product_name_from_search = search_results[pr_index].name
        product_name_from_product_page = search_results[pr_index].open_product_page().name
        assert product_name_from_search == product_name_from_product_page

    def test_search_for_empty_string(self, app, base_url):
        home_page = Home(app.driver, base_url).open()
        search_page = home_page.header.search_for("")
        assert search_page.results_count == 0
