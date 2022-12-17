from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import data
import pytest
import time

class Test_Login:
    url = "https://opensource-demo.orangehrmlive.com"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()
    
    def test_get_title(self, booting_function):
        self.driver.get(self.url)
        assert self.driver.title == "OrangeHRM"
        print("WEB TITLE CAPTURED SUCCESSFULLY")
    
    def test_login(self, booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value = data.Orange_Selectors.input_box_username).send_keys(data.Orange_Login.username)
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value = data.Orange_Selectors.input_box_password).send_keys(data.Orange_Login.password)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.login_xpath).click()
        assert self.driver.title == "OrangeHRM"
        print("LOGGED IN CAPTURED SUCCESSFULLY USING USERNAME AND PASSWORD")
