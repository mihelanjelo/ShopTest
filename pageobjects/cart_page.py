import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    
    def __init__(self, driver):
        self.driver = driver

    page_title = "Checkout | Demo Store"

    items_table_xpath = "//table[@class='items table table-striped data-table']"

    delete_item_button_xpath = "/button[@name='remove_cart_item']"

    def check_item_in_cart(self, item_name, size, quantity):
        item_name_locator = (By.XPATH, self.items_table_xpath + "//a[contains(text(), '" + item_name + "')]")
        item_name_label = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(item_name_locator))
        size_locator = (By.XPATH, self.items_table_xpath + "//div[@class='options' and contains(text(),'Size: " + size + "')]")
        size_label = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(size_locator))
        quantity_locator = (By.XPATH, self.items_table_xpath + "//input[@class='form-control' and @value='" + quantity + "']")
        quantity_input = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(quantity_locator))
        return True

    def check_item_not_in_cart(self, item_name, size, quantity):
        for i in range(0, 11):
            try:
                self.check_item_in_cart(item_name, size, quantity)
            except TimeoutException:
                return True
            time.sleep(0.5)
        return False

    def delete_item(self, item_name):
        delete_item_locator = (By.XPATH, self.items_table_xpath + "//tr[td/div/strong/a[text()='" + item_name + "']]/" + self.delete_item_button_xpath)
        delete_button = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(delete_item_locator))
        delete_button.click()
