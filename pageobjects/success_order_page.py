from selenium.webdriver.common.by import By
from .base_page import BasePage


class SuccessOrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    PAGE_TITLE = "Order Success | Demo Store"

    LOCATORS = {
        "success message": (By.XPATH, "//div[@id='box-order-success']/h1[@class='title']"),
    }
