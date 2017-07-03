from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    page_title = "Demo Store | Online Store"

    go_to_cart_locator = (By.XPATH, "//div[@class='title' and contains(text(), 'Shopping Cart')]")

    def choose_item(self, item_name, time_waiting_element=0):
        item_locator = (By.XPATH, "//a[@title='" + item_name + "']")
        item = WebDriverWait(self.driver, time_waiting_element).until(EC.element_to_be_clickable(item_locator))
        item.click()

    def go_to_cart(self, time_waiting_element=0):
        cart = WebDriverWait(self.driver, time_waiting_element).until(EC.element_to_be_clickable(self.go_to_cart_locator))
        cart.click()
