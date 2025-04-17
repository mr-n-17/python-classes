import selenium
from selenium.webdriver.common.by import By 

class Loginpage:
    def __init__(self,driver):
        self.driver=driver
        self.username_field= (By.ID,'user-name')
        self.password_field=(By.ID,'password')
        self.login_button=(By.ID,'login-button')
    
    def enter_username(self,username):
        print(username)
        self.driver.find_element(*self.username_field).send_keys(username)
    
    def enter_password(self,password):
        self.driver.find_element(*self.password_field).send_keys(password)
    
    def click_login(self):
        self.driver.find_element(*self.login_button).click()

# from selenium.webdriver.common.by import By

# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.username_field = (By.ID, "username")
#         self.password_field = (By.ID, "password")
#         self.login_button = (By.ID, "signInBtn")

#     def enter_username(self, username):
#         self.driver.find_element(*self.username_field).send_keys(username)

#     def enter_password(self, password):
#         self.driver.find_element(*self.password_field).send_keys(password)

#     def click_login(self):
#         self.driver.find_element(*self.login_button).click()
