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
