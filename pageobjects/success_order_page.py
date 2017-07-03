from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SuccessOrderPage:

    def __init__(self, driver):
        self.driver = driver

    page_title = "Order Success | Demo Store"

    success_message_locator = (By.XPATH, "//div[@id='box-order-success']/h1[@class='title']")

    def get_success_message(self, time_waiting_element=0):
        success_message = WebDriverWait(self.driver, time_waiting_element).until(EC.presence_of_element_located(self.success_message_locator))
        return success_message.text