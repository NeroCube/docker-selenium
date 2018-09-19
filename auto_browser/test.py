# -*- coding: utf-8 -*-
from common import tool
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from requests.auth import HTTPBasicAuth
import requests, unittest, json, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
          command_executor='http://localhost:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.implicitly_wait(5)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def post(self, payload, requests_url):
        token = self.get_auth_token()
        headers = tool.mockup_headers(token=token)
        response = requests.post(requests_url, data=payload.encode('utf-8'), headers=headers)
        return response.text
    
    def login_website():
        driver = self.driver
        user = tool.mockup_user()
        configs = tool.mockup_configs()
        driver.get(configs["base_url"]+"login")
        driver.find_element_by_name("email").send_keys(user["email"])
        driver.find_element_by_name("password").send_keys(user["password"])
        driver.find_element_by_name("email").send_keys(Keys.ENTER)
    
    def get_auth_token(self):
        user = tool.mockup_user()
        configs = tool.mockup_configs()
        response = requests.get(configs['auth_url'], auth=HTTPBasicAuth(user['email'], user['password']))
        obj = json.loads(response.text)
        return obj['results']['token']

    def test_login_test_case(self):
        waits = 3
        user = tool.mockup_user()
        configs = tool.mockup_configs()
        # payload = tool.mockup_payload()
        # requests_url = "requests_url"
        # response = self.post(payload, requests_url)

        driver = self.driver
        driver.get(configs["base_url"]+"login")
        driver.find_element_by_name("email").send_keys(user["email"])
        driver.find_element_by_name("password").send_keys(user["password"])
        driver.find_element_by_name("email").send_keys(Keys.ENTER)       
        time.sleep(waits)
        driver.save_screenshot(tool.get_screenshot_file_path(filename="login"))
    
    def check_element_in_page(self, target):
        start = time.time()
        while True:
            if target in self.driver.page_source:
                time.sleep(0.5)
                break
            spend = time.time() -start
            print('spend:{}'.format(spend))
            if spend > 10:
                raise  TimeoutException
            time.sleep(0.5)

    def check_element_load_finish(self, how, what):
        locator = (how, what)
        try:
            WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(locator))
        except TimeoutException as e: 
            return False
        return True

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
