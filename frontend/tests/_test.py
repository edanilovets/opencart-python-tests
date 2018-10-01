from selenium import webdriver
from frontend.pages.base import Base


driver = webdriver.Chrome()
base_url = 'http://localhost:8080/opencart'
page = Base(driver, base_url).open()
# TopLine clicking
# page.topline.click_my_account()
# page.topline.click_login()

# Search
search_page = page.header.search_for("apple")
print("Number of items found: {}".format(search_page.results_count))
print("Number of pages: {}".format(search_page.number_of_pages[-8:-7]))
print("Search results:\n{}".format(search_page.search_results))
search_page.search_results[0].open_product_page()

# search_page = page.header.search_for("sss")
# print("No result message: {}".format(search_page.no_results_message))


# driver.quit()
