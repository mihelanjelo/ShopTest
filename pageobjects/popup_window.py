from selenium.webdriver.common.by import By
from .base_page import BasePage


# Всплывающее окно при выборе товара
class PopUpWindow(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    LOCATORS = {
        "popup window": (By.CLASS_NAME, "featherlight-content"),
        "select size": (By.XPATH, "//select[@name='options[Size]']"),
        "quantity field": (By.XPATH, "//input[@name='quantity']"),
        "add to cart button": (By.XPATH, "//button[@name='add_cart_product']"),
        "close popup button": (By.XPATH, "//div[@aria-label='Close']"),
    }

    XPATH_PATTERNS = {
        "item link": "//a[@title='{item_name}']"
    }
