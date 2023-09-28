from selenium.webdriver.common.by import By

from utilities.CheckoutPage import CheckoutPage


class HomePage():

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.XPATH,"//input[@class='form-control ng-pristine ng-invalid ng-touched']")
    email = (By.XPATH, "email")
    checkbox=(By.XPATH,"//*[@id='exampleCheck1']")
    gender=(By.XPATH,"//*[@id='exampleFormControlSelect1']")
    submit=(By.XPATH,"/html/body/app-root/form-comp/div/form/input")
    successMsg=(By.CSS_SELECTOR,"[class='alert-success']")



    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage

    def getName(self):
        self.driver.find_element(*HomePage.name)

    def getEmail(self):
        self.driver.find_element(*HomePage.email)

    def getCheckbox(self):
        self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        self.driver.find_element(*HomePage.gender)

    def getSubmit(self):
        self.driver.find_element(*HomePage.submit)
    def getSuccesText(self):
        self.driver.find_element(*HomePage.successMsg)

