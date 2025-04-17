import selenium
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select

class Sauce: 
    def __init__(self,driver):
        self.driver=driver
        self.username=(By.ID,'user-name')
        self.password=(By.ID,'password')
        self.loginbutton=(By.ID,'login-button')
        self.dropdown=(By.CLASS_NAME,'product_sort_container')
        self.products=(By.CLASS_NAME,'inventory_item')
        self.product1=(By.TAG_NAME,'button')
        self.addcart=(By.XPATH,'//*[@id="shopping_cart_container"]/a')
        self.checkout=(By.ID,'checkout')
        self.firstname=(By.ID,'first-name')
        self.lastname=(By.ID,'last-name')
        self.postalcode=(By.ID,'postal-code')
        self.cont=(By.ID,'continue')
        self.fin=(By.ID,'finish')
        self.clickit=(By.ID,'react-burger-menu-btn')
        self.logout1=(By.ID,'logout_sidebar_link')
    
    def dropdown1(self,text):
        f=self.driver.find_element(*self.dropdown)
        c=Select(f)
        f.select_by_visible_text(text) 
    
    def addiems(self,button):
        p=self.driver.find_element(*self.products)
        p[0].find_element(*self.products1).click()
        p[-1].find_element(*self.products1).click()

    def addcartit(self):
        self.driver.find_element(*self.addcart).click()


    if (self.driver.find_element(By.CLASS_NAME,'shopping_cart_badge')).text=='2':


def dropdown1(self,text):
dropdown=d.find_element(By.CLASS_NAME,'product_sort_container')
f=Select(dropdown)
time.sleep(2)
f.select_by_visible_text('Price (low to high)') #text
time.sleep(2)

def addiems(self,button)
product=d.find_elements(By.CLASS_NAME,'inventory_item')
product[0].find_element(By.TAG_NAME,'button').click()
time.sleep(1)
product[-1].find_element(By.TAG_NAME,'button').click()
time.sleep(1)
# p1=d.find_element(By.ID,'add-to-cart-sauce-labs-onesie').click()

# time.sleep(1)

# p2=d.find_element(By.ID,'add-to-cart-sauce-labs-fleece-jacket').click()

# time.sleep(1)

def addcartit(self)
addcart=d.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a').click()

time.sleep(1)

if (d.find_element(By.CLASS_NAME,'shopping_cart_badge')).text=='2':

    def checkoutit(self,checkout)
    checkout=d.find_element(By.ID,'checkout').click()

    time.sleep(1) 
    
    def firstname1(self,fname)
    firstname=d.find_element(By.ID,'first-name').send_keys('Test')

    time.sleep(1)

    def lastname1(self,lname)
    lastname=d.find_element(By.ID,'last-name').send_keys('User')

    time.sleep(1)

    def postal1(self,code1)
    postal=d.find_element(By.ID,'postal-code').send_keys("12345")

    time.sleep(1)
    
    def continuebutton(self)
    con=d.find_element(By.ID,'continue').click()

    time.sleep(1)

    def finishbutton(self)
    fin=d.find_element(By.ID,'finish').click()

    time.sleep(1)

    def backtobutton(self)
    backto=d.find_element(By.ID,"back-to-products").click()

    time.sleep(1)
    
    def sidebarbutton(self)
    clickit=d.find_element(By.ID,'react-burger-menu-btn').click()

    time.sleep(1)

    def logoutbutton(self)
    logout1=d.find_element(By.ID,'logout_sidebar_link').click()
else:
    raise 'THE CART SHOULD HAVE Two ITEMS/QUANTITIES'