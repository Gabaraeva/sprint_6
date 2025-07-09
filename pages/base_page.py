from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import URLs


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = URLs.MAIN_PAGE

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Не найден элемент по локатору {locator}"
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Не найдены элементы по локатору {locator}"
        )

    def click_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент по локатору {locator} не кликабелен"
        )
        element.click()

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент по локатору {locator} не стал кликабельным"
        )

    # ДОБАВЛЕНО: Метод для ожидания видимости элемента
    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент по локатору {locator} не стал видимым"
        )

    # ДОБАВЛЕНО: Метод для ожидания количества окон
    def wait_for_number_of_windows(self, number, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) == number,
            message=f"Количество окон не стало равным {number}"
        )

    # ДОБАВЛЕНО: Метод для проверки содержания текста в URL
    def is_url_contains(self, text):
        return text in self.driver.current_url

    def go_to_site(self):
        self.driver.get(self.base_url)

    def get_current_url(self):
        return self.driver.current_url

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def switch_to_new_window(self, current_handle):
        self.wait_for_number_of_windows(2)
        new_window = [window for window in self.driver.window_handles if window != current_handle][0]
        self.driver.switch_to.window(new_window)
        return new_window