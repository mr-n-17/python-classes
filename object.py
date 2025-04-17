from selenium import webdriver
from login import Loginpage 
import time

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
k=Loginpage(driver) 

k.enter_username('standard_user')
time.sleep(2)
k.enter_password('secret_sauce')
time.sleep(2)
k.click_login()

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from login import LoginPage
# import time


# #chrome_driver_path = "C:\development\chromedriver.exe"  # Ensure double backslashes
# # service=Service(executable_path="chromedriver.exe")
# # driver = webdriver.Chrome(service=service)
# driver=webdriver.Chrome()


# # from webdriver_manager.chrome import ChromeDriverManager
# #
# # driver = webdriver.Chrome(ChromeDriverManager().install())

# # chrome_driver_path="C:\development\chromedriver.exe"
# #
# # driver=webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/loginpagePractise/")

# login_page = LoginPage(driver)
# login_page.enter_username("rahulshettyacademy")
# time.sleep(1)
# login_page.enter_password("learning")
# time.sleep(2)
# login_page.click_login()

# # driver.quit()