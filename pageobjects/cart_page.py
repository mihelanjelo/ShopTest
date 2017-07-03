import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    page_title = "Checkout | Demo Store"

    items_table_xpath = "//table[@class='items table table-striped data-table']"
    delete_item_button_xpath = "/button[@name='remove_cart_item']"
    account_created_alert_locator = (By.XPATH, "//div[@class='alert alert-success']")
    account_exists_alert_locator = (By.XPATH, "//div[@class='alert alert-info']")
    tax_id_field_locator = (By.XPATH, "//input[@name='tax_id']")
    company_field_locator = (By.XPATH, "//input[@name='company']")
    first_name_field_locator = (By.XPATH, "//input[@name='firstname']")
    last_name_field_locator = (By.XPATH, "//input[@name='lastname']")
    address1_field_locator = (By.XPATH, "//input[@name='address1']")
    address2_field_locator = (By.XPATH, "//input[@name='address2']")
    postcode_field_locator = (By.XPATH, "//input[@name='postcode']")
    city_field_locator = (By.XPATH, "//input[@name='city']")
    country_field_locator = (By.XPATH, "//select[@name='country_code']")
    email_field_locator = (By.XPATH, "//input[@name='email']")
    phone_field_locator = (By.XPATH, "//input[@name='phone']")
    desired_password_field_locator = (By.XPATH, "//input[@name='password']")
    confirmed_password_field_locator = (By.XPATH, "//input[@name='confirmed_password']")
    create_account_checkbox_locator = (By.XPATH, "//input[@name='create_account']")
    save_changes_button_locator = (By.XPATH, "//button[@name='save_customer_details']")
    confirm_order_button_locator = (By.XPATH, "//button[@name='confirm_order']")
    changes_quantity_xpath = "/input[@class='form-control' and @type='number']"

    def check_item_in_cart(self, item_name, size, quantity, time_waiting_element=0):
        item_name_locator = (By.XPATH, self.items_table_xpath + "//a[contains(text(), '" + item_name + "')]")
        item_name_label = WebDriverWait(self.driver, time_waiting_element).until(EC.visibility_of_element_located(item_name_locator))
        size_locator = (
        By.XPATH, self.items_table_xpath + "//div[@class='options' and contains(text(),'Size: " + size + "')]")
        size_label = WebDriverWait(self.driver, time_waiting_element).until(EC.visibility_of_element_located(size_locator))
        quantity_locator = (
        By.XPATH, self.items_table_xpath + "//input[@class='form-control' and @value='" + quantity + "']")
        quantity_input = WebDriverWait(self.driver, time_waiting_element).until(EC.visibility_of_element_located(quantity_locator))
        return True

    def check_item_not_in_cart(self, item_name, size, quantity, time_waiting_element=0):
        for i in range(0, 11):
            try:
                self.check_item_in_cart(item_name, size, quantity, time_waiting_element)
            except TimeoutException:
                return True
            time.sleep(0.5)
        return False

    def delete_item(self, item_name, time_waiting_element=0):
        delete_item_locator = (By.XPATH,
                               self.items_table_xpath + "//tr[td/div/strong/a[text()='" + item_name + "']]/" + self.delete_item_button_xpath)
        delete_button = WebDriverWait(self.driver, time_waiting_element).until(EC.element_to_be_clickable(delete_item_locator))
        delete_button.click()

    def set_tax_id(self, tax_id, time_waiting_element=0):
        tax_id_field = WebDriverWait(self.driver, time_waiting_element).until(EC.element_to_be_clickable(self.tax_id_field_locator))
        tax_id_field.clear()
        tax_id_field.send_keys(tax_id)

    def set_company(self, company, time_waiting_element=0):
        company_field = WebDriverWait(self.driver, time_waiting_element).until(EC.element_to_be_clickable(self.company_field_locator))
        company_field.clear()
        company_field.send_keys(company)

    def set_first_name(self, first_name, time_waiting_element=0):
        first_name_field = WebDriverWait(self.driver, time_waiting_element).until(
            EC.element_to_be_clickable(self.first_name_field_locator))
        first_name_field.clear()
        first_name_field.send_keys(first_name)

    def set_last_name(self, last_name, time_waiting_element=0):
        last_name_field = WebDriverWait(self.driver, time_waiting_element).until(
            EC.element_to_be_clickable(self.last_name_field_locator))
        last_name_field.clear()
        last_name_field.send_keys(last_name)

    def set_address1(self, address1, time_waiting_element=0):
        address1_field = WebDriverWait(self.driver, time_waiting_element).until(
            EC.element_to_be_clickable(self.address1_field_locator))
        address1_field.clear()
        address1_field.send_keys(address1)

    def set_address2(self, address2, time_waiting_element=0):
        address2_field = WebDriverWait(self.driver, time_waiting_element).until(
            EC.element_to_be_clickable(self.address2_field_locator))
        address2_field.clear()
        address2_field.send_keys(address2)

    def set_postcode(self, postcode, time_waiting_element=0):
        postcode_field = WebDriverWait(self.driver, time_waiting_element).until(
            EC.element_to_be_clickable(self.postcode_field_locator))
        postcode_field.clear()
        postcode_field.send_keys(postcode)

    def set_city(self, city, time_waiting_element=0):
        city_field = WebDriverWait(self.driver, time_waiting_element).until(
            EC.element_to_be_clickable(self.city_field_locator))
        city_field.clear()
        city_field.send_keys(city)

    def set_country(self, country, time_waiting_element=0):
        country_field = Select(WebDriverWait(self.driver, time_waiting_element).until(
            EC.presence_of_element_located(self.country_field_locator)))
        country_field.select_by_visible_text(country)

    def set_email(self, email, time_waiting_element=0):
        email_field = WebDriverWait(self.driver, time_waiting_element).until(
            EC.element_to_be_clickable(self.email_field_locator))
        email_field.clear()
        email_field.send_keys(email)

    def set_phone(self, phone, time_waiting_element=0):
        phone_field = WebDriverWait(self.driver, time_waiting_element).until(
            EC.element_to_be_clickable(self.phone_field_locator))
        phone_field.clear()
        phone_field.send_keys(phone)

    def select_create_account_checkbox(self, time_waiting_element=0):
        create_account_checkbox = WebDriverWait(self.driver, time_waiting_element).until(
            EC.element_to_be_clickable(self.create_account_checkbox_locator))
        if not create_account_checkbox.is_selected():
            create_account_checkbox.click()

    def set_desired_password(self, desired_password, time_waiting_element=0):
        desired_password_field = WebDriverWait(self.driver, time_waiting_element).until(
            EC.element_to_be_clickable(self.desired_password_field_locator))
        desired_password_field.clear()
        desired_password_field.send_keys(desired_password)

    def set_confirmed_password(self, confirmed_password, time_waiting_element=0):
        confirmed_password_field = WebDriverWait(self.driver, time_waiting_element).until(
            EC.element_to_be_clickable(self.confirmed_password_field_locator))
        confirmed_password_field.clear()
        confirmed_password_field.send_keys(confirmed_password)

    def click_save_changes_button(self, time_waiting_element=0):
        save_changes_button = WebDriverWait(self.driver, time_waiting_element).until(
            EC.element_to_be_clickable(self.save_changes_button_locator))
        save_changes_button.click()

    def is_account_created_alert_visible(self, time_waiting_element=0):
        account_created_alert = WebDriverWait(self.driver, time_waiting_element).until(
            EC.visibility_of_element_located(self.account_created_alert_locator))
        return account_created_alert.is_displayed()

    def is_account_exist_alert_visible(self, time_waiting_element=0):
        account_exists_alert = WebDriverWait(self.driver, time_waiting_element).until(
            EC.visibility_of_element_located(self.account_exists_alert_locator))
        return account_exists_alert.is_displayed()

    def change_item_quantity(self, item_name, new_quantity, time_waiting_element=0):
        change_item_locator = (By.XPATH,
                               self.items_table_xpath + "//tr[td/div/strong/a[text()='" + item_name + "']]/" + self.changes_quantity_xpath)
        change_item_input = WebDriverWait(self.driver, time_waiting_element).until(EC.element_to_be_clickable(change_item_locator))
        change_item_input.clear()
        change_item_input.send_keys(new_quantity)

    def get_item_sum(self, item_name, time_waiting_element=0):
        item_sum_locator = (By.XPATH, self.items_table_xpath + "//tr[td/div/strong/a[text()='" + item_name + "']]/td[5]")
        item_sum = WebDriverWait(self.driver, time_waiting_element).until(
            EC.visibility_of_element_located(item_sum_locator))
        return round(float(item_sum.text.replace("$", "")), 2)

    def click_refresh_item_button(self, item_name, time_waiting_element=0):
        item_refresh_locator = (By.XPATH, self.items_table_xpath + "//tr[td/div/strong/a[text()='" + item_name + "']]//i[@class='fa fa-refresh']")
        item_refresh = WebDriverWait(self.driver, time_waiting_element).until(
            EC.element_to_be_clickable(item_refresh_locator))
        item_refresh.click()

    def click_confirm_order_button(self, time_waiting_element=0):
        confirm_order_button = WebDriverWait(self.driver, time_waiting_element).until(
            EC.element_to_be_clickable(self.confirm_order_button_locator))
        confirm_order_button.click()
