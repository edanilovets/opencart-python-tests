from selenium import webdriver

# Chrome options https://peter.sh/experiments/chromium-command-line-switches/
# Firefox options https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("")
wd = webdriver.Chrome(chrome_options=chrome_options)
wd.get("http://localhost:8080/opencart/")

# Getting element properties and attributes
print(wd.find_element_by_id("menu").value_of_css_property("min-height"))
print(wd.find_element_by_id("menu").location)
print(wd.find_element_by_id("menu").size)
print(wd.find_element_by_id("menu").tag_name)
print(wd.find_element_by_id("menu").text)
print(wd.find_element_by_id("menu").get_attribute("id"))

# Performing actions on elements
input_email = wd.find_element_by_css_selector("#input-email")
input_email.send_keys("value")
input_email.send_keys(Keys.SHIFT, "hello")
input_email.send_keys(Keys.TAB)
input_password = wd.find_element_by_css_selector("#input-password")
input_password.send_keys(Keys.SHIFT, "hello")
input_password.clear()
input_password.submit()

# Check elements state
login_button = wd.find_element_by_css_selector("#content > div > div:nth-child(2) > div > form > input")
subscribe_radio = wd.find_element_by_css_selector(
    "#content > form > fieldset > div > div > label:nth-child(2) > input[type='radio']")
print(login_button.is_displayed())
print(login_button.is_enabled())
print(subscribe_radio.is_selected())    # only for radio button, options in select, or a checkbox

# Actions





