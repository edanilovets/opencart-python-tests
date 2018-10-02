from frontend.pages.home_page import Home


class TestSearch:
    def test_search_results_is_shown(self, app, base_url):
        home_page = Home(app.driver, base_url).open()
        search_page = home_page.header.search_for("apple")
        assert search_page.results_count > 0

    def test_can_open_product_from_search_results(self, app, base_url):
        home_page = Home(app.driver, base_url).open()
        search_page = home_page.header.search_for("apple")
        product_page = search_page.search_results[0].open_product_page()
        assert search_page.search_results[0].name == product_page.name
