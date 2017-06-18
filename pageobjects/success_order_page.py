from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SuccessOrderPage:

    def __init__(self, driver):
        self.driver = driver

    page_title = "Order Success | Demo Store"

    success_message_locator = (By.XPATH, "//div[@id='box-order-success']/h1[@class='title']")

    def get_success_message(self):
        success_message = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.success_message_locator))
        return success_message.text