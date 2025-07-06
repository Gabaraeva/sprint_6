from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import URLs  # Импортируем URL из конфигурационного файла


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = URLs.MAIN_PAGE  # Используем константу из config.py

    def find_element(self, locator, time=10):
        """Поиск элемента с явным ожиданием"""
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Не найден элемент по локатору {locator}"
        )

    def find_elements(self, locator, time=10):
        """Поиск нескольких элементов"""
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Не найдены элементы по локатору {locator}"
        )

    def click_element(self, locator):
        """Клик по элементу с явным ожиданием кликабельности"""
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент по локатору {locator} не кликабелен"
        )
        element.click()

    def scroll_to_element(self, locator):
        """Прокрутка страницы к элементу"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def wait_for_element_clickable(self, locator, timeout=10):
        """Ожидание кликабельности элемента"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент по локатору {locator} не стал кликабельным"
        )

    def go_to_site(self):
        """Переход на базовый URL"""
        self.driver.get(self.base_url)

    def get_current_url(self):
        """Получение текущего URL"""
        return self.driver.current_url

    def switch_to_new_window(self, current_handle):
        """Переключение на новое окно/вкладку"""
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        new_window = [window for window in self.driver.window_handles if window != current_handle][0]
        self.driver.switch_to.window(new_window)
        return new_window