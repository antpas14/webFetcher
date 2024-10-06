from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import os
import re
import configparser
from datetime import datetime
from datetime import timezone

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

    def get_url(self, url, cookies):
        """ Get url and uses cookies passed to it. If no cookies are passed they will not be used
        Note that does a dummy request to allow cookies to be set

        :param url: url to request
        :type url: str
        :param cookies: cookies passed to it. If no cookies are passed they will not be used
        :type cookies: dict

        :return: source of web page"""
        fake_url = self.extract_base_url(url) + "/dummylink"
        self.driver.get(fake_url)
        self.add_cookies_to_webdriver(cookies)
        self.driver.get(url)
        return self.driver.page_source

    def extract_base_url(self, url):
        """Extracts the base URL (protocol and domain) from a given URL.

        Args:
            url: The URL string.

        Returns:
            The extracted base URL (protocol + domain) or None if no valid base URL is found.
        """
        pattern = r"(https?://[^\s]+)"
        match = re.search(pattern, url)
        if match:
            return match.group(1)
        else:
            return None

    def parse_cookie_dict(self, cookie_dict):
        """Parses a cookie dictionary into a format compatible with WebDriver.

        Args:
            cookie_dict: A dictionary representing a single cookie.

        Returns:
            A dictionary suitable for adding to WebDriver's cookie store.
        """

        parsed_cookie = {
            'name': cookie_dict['name'],
            'value': cookie_dict['value'],
            'domain': cookie_dict['domain'],
            'path': cookie_dict['path'],
        }

        # Convert expiration date from epoch milliseconds to datetime object
        if 'expirationDate' in cookie_dict:
            expiration_time = datetime.fromtimestamp(cookie_dict['expirationDate'], timezone.utc)
            parsed_cookie['expires'] = expiration_time.strftime('%a, %d-%b-%Y %H:%M:%S GMT')

        # Set other optional attributes based on the dictionary keys
        parsed_cookie['secure'] = cookie_dict.get('secure', False)  # Default to False
        parsed_cookie['httpOnly'] = cookie_dict.get('httpOnly', True)  # Default to True
        # ... (add other optional attributes if needed)

        return parsed_cookie

    def add_cookies_to_webdriver(self, cookie_list):
        """Adds a list of cookies to the WebDriver instance.

        Args:
            driver: The WebDriver instance.
            cookie_list: A list of dictionaries representing cookies.
        """

        for cookie_dict in cookie_list:
            parsed_cookie = self.parse_cookie_dict(cookie_dict)
            try:
                self.driver.add_cookie(parsed_cookie)
            except Exception as e:
                print("Cookie could not be added to WebDriver:", parsed_cookie, e)
