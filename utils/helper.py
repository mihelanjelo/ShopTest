import time
from selenium import webdriver


class Helper:

    def __init__(self, browser_name, executable_path):
        self.driver = Helper.choose_browser(browser_name, executable_path=executable_path)
        self.driver.set_window_size(1920, 1080)
        self.driver.implicitly_wait(4)

    def visit(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

    def is_page_opened(self, page, waiting_time=0):
        for i in range(0, waiting_time + 1):
            if self.driver.title == page.PAGE_TITLE:
                return True
            elif i == waiting_time:
                return False
            else:
                time.sleep(1)

    def refresh(self):
        self.driver.refresh()

    @staticmethod
    def choose_browser(browser, executable_path):
        if browser == "Chrome":
            if not executable_path: return webdriver.Chrome()
            return webdriver.Chrome(executable_path=executable_path)
        elif browser == "Firefox":
            if not executable_path: return webdriver.Firefox()
            return webdriver.Firefox(executable_path=executable_path)
        else:
            raise ValueError("Неверное имя браузера!")
