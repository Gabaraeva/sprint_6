import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.order_page import OrderPage
from test_data import OrderData  # Импортируем тестовые данные из отдельного модуля


@allure.feature("Тесты заказа самоката")
class TestOrder:

    @allure.title("Тест заказа самоката через верхнюю кнопку")
    def test_order_scooter_top_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.accept_cookies()

        with allure.step("Нажимаем верхнюю кнопку 'Заказать'"):
            main_page.click_order_button_top()

        with allure.step("Заполняем первую страницу заказа"):
            order_page.fill_first_page(**OrderData.TOP_ORDER['user_data'])

        with allure.step("Заполняем вторую страницу заказа"):
            order_page.fill_second_page(**OrderData.TOP_ORDER['order_data'])

        with allure.step("Проверяем подтверждение заказа"):
            assert order_page.is_order_successful(), "Заказ не был успешно оформлен"

    @allure.title("Тест заказа самоката через нижнюю кнопку")
    def test_order_scooter_bottom_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.accept_cookies()

        with allure.step("Нажимаем нижнюю кнопку 'Заказать'"):
            # Используем метод Page Object вместо прямого вызова driver
            main_page.scroll_to_bottom_button()
            main_page.click_order_button_bottom()

        with allure.step("Заполняем первую страницу заказа"):
            order_page.fill_first_page(**OrderData.BOTTOM_ORDER['user_data'])

        with allure.step("Заполняем вторую страницу заказа"):
            order_page.fill_second_page(**OrderData.BOTTOM_ORDER['order_data'])

        with allure.step("Проверяем подтверждение заказа"):
            assert order_page.is_order_successful(), "Заказ не был успешно оформлен"

    @allure.title("Проверка перехода по логотипу Самоката")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()

        with allure.step("Нажимаем на логотип Самоката"):
            main_page.click_scooter_logo()

        with allure.step("Проверяем URL"):
            assert driver.current_url == "https://qa-scooter.praktikum-services.ru/", \
                f"Ожидался URL https://qa-scooter.praktikum-services.ru/, получен {driver.current_url}"

    @allure.title("Проверка перехода по логотипу Яндекса")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()

        current_window = driver.current_window_handle

        with allure.step("Нажимаем на логотип Яндекса"):
            main_page.click_yandex_logo()

        with allure.step("Ожидаем открытия новой вкладки"):
            # Используем явное ожидание вместо фиксированной паузы
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
            new_window = [window for window in driver.window_handles if window != current_window][0]

        with allure.step("Переключаемся на новую вкладку"):
            driver.switch_to.window(new_window)

        with allure.step("Ожидаем загрузки Дзена"):
            # Используем более надежный локатор
            WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located(("css selector", "div.dzen-desktop"))
            )

        with allure.step("Проверяем URL"):
            assert "dzen.ru" in driver.current_url, \
                f"URL {driver.current_url} не содержит 'dzen.ru'"