from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import configparser

if os.environ.get('DOCKER'):
    config_file = 'config.docker.ini'
else:
    config_file = 'config.local.ini'

config = configparser.ConfigParser()
config.read(config_file)


class Webdriver:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-extensions')

        chrome_driver_path = config['webdriver']['chrome_driver_path']
        service = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=service, options=options)

    def get_url(self, url):
        self.driver.get(url)
        return self.driver.page_source
