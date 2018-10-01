from selenium import webdriver
from frontend.pages.base import Base


driver = webdriver.Chrome()
base_url = 'http://localhost:8080/opencart'
page = Base(driver, base_url).open()

# TopLine
# page.topline.click_my_account()
# page.topline.click_login()
# print("Is Login menu item present: {}".format(page.topline.is_login_menu_item_present))
# print("Is Logout menu item present: {}".format(page.topline.is_logout_menu_item_present))

# Cart
# print("Cart results: {}".format(page.header.cart_results))

# Search
search_page = page.header.search_for("apple")
# search_page = page.header.search_for("sss")
# print("No result message: {}".format(search_page.no_results_message))
print("Number of items found: {}".format(search_page.results_count))
print("Number of pages: {}".format(search_page.number_of_pages))
print("Search results: {}".format(search_page.search_results))
print("Name[5]: {}".format(search_page.search_results[5].name))
product_page = search_page.search_results[5].open_product_page()
# product_page = search_page.search_results[3].open_product_page()
print("Product name: {}".format(product_page.name))

# Cart
product_page.click_add_to_cart()
product_page.header.click_on_cart()
print("Is cart popup displayed? {}".format(product_page.header.is_cart_popup_displayed))
print("Cart results: {}".format(product_page.header.cart_results))

# driver.quit()
