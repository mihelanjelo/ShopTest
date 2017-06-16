import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Helper:

    def __init__(self, browser_name):
        self.driver = Helper.choose_browser(browser_name)

    def visit(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.quit()

    def wait_to_be_visible(self, locator, time_sec):
        return WebDriverWait(self.driver, time_sec).until(EC.visibility_of_element_located(locator))

    def wait_not_visible(self, locator, time_sec):
        try:
            for i in range(0, time_sec + 1):
                if WebDriverWait(self.driver, 0.5).until(EC.visibility_of_element_located(locator)):
                    time.sleep(0.5)
                elif i == time_sec:
                    return False
        except TimeoutException:
            return True

    def wait_page(self, page, waiting_time):
        for i in range(0, waiting_time + 1):
            if self.driver.title == page.page_title:
                break
            elif i == 5:
                raise Exception("Page isn't visible for " + waiting_time + "sec!")
            else:
                time.sleep(1)

    @staticmethod
    def choose_browser(browser):
        if browser == "Chrome":
            return webdriver.Chrome()
        elif browser == "Firefox":
            return webdriver.Firefox()
        elif browser == "IE":
            return webdriver.Ie()
