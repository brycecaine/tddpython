from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")
browser = webdriver.Firefox(firefox_options=options)
browser.get('http://localhost:8000')
# browser.get('http://35.185.203.248:8000')
# browser.get('http://10.138.0.3:8000')

assert 'Django' in browser.title
