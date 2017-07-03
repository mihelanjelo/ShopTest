from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# Всплывающее окно при выборе товара
class PopUpWindow:
    def __init__(self, driver):
        self.driver = driver

    popup_window_locator = (By.CLASS_NAME, "featherlight-content")
    select_locator = (By.XPATH, "//select[@name='options[Size]']")
    quantity_locator = (By.XPATH, "//input[@name='quantity']")
    add_to_cart_locator = (By.XPATH, "//button[@name='add_cart_product']")
    close_locator = (By.XPATH, "//button[@aria-label='Close']")

    def select_size_by_value(self, size, time_waiting_element=0):
        select = Select(WebDriverWait(self.driver, time_waiting_element).until(EC.presence_of_element_located(self.select_locator)))
        select.select_by_visible_text(size)

    def select_size_by_order(self, size, time_waiting_element=0):
        select = Select(WebDriverWait(self.driver, time_waiting_element).until(EC.presence_of_element_located(self.select_locator)))
        select.select_by_index(size)

    def input_quantity(self, quantity, time_waiting_element=0):
        input_quantity = WebDriverWait(self.driver, time_waiting_element).until(EC.element_to_be_clickable(self.quantity_locator))
        input_quantity.clear()
        input_quantity.send_keys(quantity)

    def add_to_cart(self, time_waiting_element=0):
        add_to_cart_button = WebDriverWait(self.driver, time_waiting_element).until(EC.element_to_be_clickable(self.add_to_cart_locator))
        add_to_cart_button.click()

    def close(self, time_waiting_element=0):
        close_button = WebDriverWait(self.driver, time_waiting_element).until(EC.element_to_be_clickable(self.close_locator))
        close_button.click()
