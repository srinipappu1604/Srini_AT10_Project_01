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
    
    def test_add_employee(self, booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value = data.Orange_Selectors.input_box_username).send_keys(data.Orange_Login.username)
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value = data.Orange_Selectors.input_box_password).send_keys(data.Orange_Login.password)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.login_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.pim_module_click).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.pim_add_click).click()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value = data.Orange_Selectors.first_name).send_keys(data.Add_New_Employee.firstname)
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value = data.Orange_Selectors.middle_name).send_keys(data.Add_New_Employee.middlename)
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value = data.Orange_Selectors.last_name).send_keys(data.Add_New_Employee.lastname)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.first_save).click()
        time.sleep(10)
        self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.nick_name).send_keys(data.Add_New_Employee.nickname)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.drivers_license_number).send_keys(data.Add_New_Employee.driverslicencenumber)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.license_expiry_date).send_keys(data.Add_New_Employee.licenseexpirydate)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.ssn_number).send_keys(data.Add_New_Employee.ssnnumber)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.sin_number).send_keys(data.Add_New_Employee.sinnumber)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.nationality_dropdown).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.marital_status).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.date_of_birth).send_keys(data.Add_New_Employee.dateofbirth)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.gender_male).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.military_service).send_keys(data.Add_New_Employee.militaryservice)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value = data.Orange_Selectors.final_save).click()
        assert self.driver.title == "OrangeHRM"
        print("NEW EMPLOYEE ADDED SUCCESSFULLY")
        
