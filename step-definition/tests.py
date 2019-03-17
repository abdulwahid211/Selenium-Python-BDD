import os
from selenium.webdriver.common.keys import Keys
from webdrivers.firefox import Firefox

ROOT_DIR = os.path.abspath(os.curdir)

Firefox = Firefox()
Firefox.FireFoxBrowser()
browser = Firefox.FireFoxBrowser()

browser.get('https://www.google.com')
assert 'Google' in browser.title

elem = browser.find_element_by_name("q")  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()


