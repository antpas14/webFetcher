from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class Webdriver:
  def __init__(self):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

  def get_url(self, url):
    self.driver.get(url)
    return self.driver.page_source