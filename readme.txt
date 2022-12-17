This is a Project Folder for "AT_Project_01"

There are two Folder:-

1.) Test_Codes # It consists of Test Files

2.) Test_Data # it consists of Test Data's i.e. username, password, XPATH, ID, etc

NOTE # If you want to run a Test File Kindly go to the Test_Codes to run a specific Python Selenium Automation File.


COMMAND TO RUN A TEST FILE
--------------------------

pytest -v -s test_login.py
pytest -v -s invalid_login.py
pytest -v -s add_employee.py
pytest -v -s edit_existing_employee.py
pytest -v -s delete_existing_employee.py

pytest -v -s --capture=sys --html=C:\pytest_reports\testloginreport.html test_login.py
pytest -v -s --capture=sys --html=C:\pytest_reports\testinvalidloginreport.html invalid_login.py
pytest -v -s --capture=sys --html=C:\pytest_reports\addemployee.py.html add_employee.py
pytest -v -s --capture=sys --html=C:\pytest_reports\editexistingemployee.py.html edit_existing_employee.py
pytest -v -s --capture=sys --html=C:\pytest_reports\deleteexistingemployee.html delete_existing_employee.py