from frontend.pages.home_page import Home


class TestSearch:
    def test_search_results_for_not_logged_in_customer(self, app, base_url):
        home_page = Home(app.driver, base_url).open()