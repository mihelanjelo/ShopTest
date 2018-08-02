from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    PAGE_TITLE = "Checkout | Demo Store"

    LOCATORS = {
        'tax_id field': (By.XPATH, "//input[@name='tax_id']"),
        'company field': (By.XPATH, "//input[@name='company']"),
        'first_name field': (By.XPATH, "//input[@name='firstname']"),
        'last_name field': (By.XPATH, "//input[@name='lastname']"),
        'address1 field': (By.XPATH, "//input[@name='address1']"),
        'address2 field': (By.XPATH, "//input[@name='address2']"),
        'postcode field': (By.XPATH, "//input[@name='postcode']"),
        'city field': (By.XPATH, "//input[@name='city']"),
        'country field': (By.XPATH, "//select[@name='country_code']"),
        'email field': (By.XPATH, "//input[@name='email']"),
        'phone field': (By.XPATH, "//input[@name='phone']"),
        'create_account_checkbox': (By.XPATH, "//input[@name='create_account']"),
        'desired password field': (By.XPATH, "//input[@name='password']"),
        'confirmed password field': (By.XPATH, "//input[@name='confirmed_password']"),
        'save changes button': (By.XPATH, "//button[@name='save_customer_details']"),
        'account created alert': (By.XPATH, "//div[@class='alert alert-success']"),
        'account exists alert': (By.XPATH, "//div[@class='alert alert-info']"),
        'confirm order button': (By.XPATH, "//button[@name='confirm_order']"),
    }

    XPATH_PATTERNS = {
        "item in cart": "//tr[.//a[contains(text(), "
                        "'{item_name}')] and .//div[@class='options' and contains(text(),'{size}')] and .//input["
                        "@class='form-control' and @value='{quantity}']]",
        "delete item from cart button": "//tr[.//a[contains(text(), '{item_name}')]]//button[@name='remove_cart_item']",
        "change item quantity field": "//tr[.//a[contains(text(), '{item_name}')]]//input[@class='form-control' and "
                                      "@type='number']",
        "item sum field": "//tr[.//a[contains(text(), '{item_name}')]]/td[5]",
        "item refresh button": "//tr[.//a[contains(text(), '{item_name}')]]//i[@class='fa fa-refresh']",
    }
