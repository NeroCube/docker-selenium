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
import requests, unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
          command_executor='http://localhost:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_test_case(self):
        driver = self.driver
        user = tool.get_user_info()
        test_settings = tool.mockup_test_info()
        file_path = tool.get_screenshot_file_path()
        driver.get(test_settings["base_url"]+"login")
        driver.find_element_by_name("email").send_keys(user["email"])
        driver.find_element_by_name("password").send_keys(user["password"])
        driver.find_element_by_name("email").send_keys(Keys.ENTER)
        
        self.check_login_success(By.CLASS_NAME, test_settings["flag_login_success"])
        
        driver.save_screenshot(file_path)
        
        payload = tool.mockup_answer()[0]
        headers = tool.mockup_headers()
        response = requests.post(test_settings["api_url"], data=payload.encode('utf-8'), headers=headers)
        print("response:{}".format(str(response.text)))
    
    def check_login_success(self, how, what):
        locator = (how, what)
        try:
            WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(locator))
        except TimeoutException as e: return False
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
