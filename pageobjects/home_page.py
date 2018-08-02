from selenium.webdriver.common.by import By
from .base_page import BasePage


# Класс с элементами домашней страницы
class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    PAGE_TITLE = "Demo Store | Online Store"

    LOCATORS = {
        "go to cart link": (By.ID, "cart"),
    }

    XPATH_PATTERNS = {
        "item link": "//a[.//img[@alt='{item_name}']]"
    }
