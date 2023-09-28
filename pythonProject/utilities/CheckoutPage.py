from selenium.webdriver.common.by import By

from utilities.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    titles = (By.CSS_SELECTOR, ".card-title a")
    Name = (By.CSS_SELECTOR, ".card-footer button")
    Checkout = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.titles)  # Use find_elements to get a list of elements

    def getName(self):
        return self.driver.find_elements(*CheckoutPage.Name)  # Use find_elements to get a list of elements

    def CheckoutItems(self):
        self.driver.find_element(*CheckoutPage.Checkout).click()
        confirmpage = ConfirmPage()
        return confirmpage
