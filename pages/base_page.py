from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Не найден элемент по локатору {locator}"
        )

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def go_to_site(self):
        return self.driver.get(self.base_url)