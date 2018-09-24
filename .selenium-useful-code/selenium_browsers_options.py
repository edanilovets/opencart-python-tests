from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

# Chrome options https://peter.sh/experiments/chromium-command-line-switches/
# Firefox options https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options

chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("")
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("http://localhost:8080/opencart/")
for i in driver.get_cookies():
    print(i)
