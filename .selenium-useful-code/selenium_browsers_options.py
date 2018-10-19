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

# using custom profile to start Firefox with
# firefox_profile = webdriver.FirefoxProfile(
# "C:\\Users\\Evgeniy Danilovets\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\p0dfg3xg.custom_profile1")
# firefox_options = webdriver.FirefoxOptions()
# firefox_options.add_argument("--devtools")
# firefox_options.add_argument("--headless")
# binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
# self.wd = webdriver.Firefox(firefox_binary=binary,
#                             options=firefox_options, firefox_profile=firefox_profile)
# self.wd = webdriver.Firefox(firefox_binary=binary)
