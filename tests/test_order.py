import pytest
import allure
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Тесты заказа самоката")
class TestOrder:
    ORDER_DATA = [
        (
            "top",  # точка входа (верхняя кнопка)
            {
                "name": "Иван",
                "last_name": "Иванов",
                "address": "Москва, Красная площадь",
                "metro_station": "Лубянка",
                "phone": "88005553535"
            },
            {
                "date": "01.01.2025",
                "period": "сутки",
                "color": "black",
                "comment": "Первый тестовый заказ"
            }
        ),
        (
            "bottom",  # точка входа (нижняя кнопка)
            {
                "name": "Петр",
                "last_name": "Петров",
                "address": "Санкт-Петербург, Дворцовая площадь",
                "metro_station": "Адмиралтейская",
                "phone": "89001234567"
            },
            {
                "date": "15.01.2025",
                "period": "двое суток",
                "color": "grey",
                "comment": "Второй тестовый заказ"
            }
        )
    ]

    @allure.title("Тест заказа самоката через {entry_point}")
    @pytest.mark.parametrize("entry_point, user_data, order_data", ORDER_DATA)
    def test_order_scooter(self, driver, entry_point, user_data, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.accept_cookies()

        with allure.step(f"Нажимаем кнопку 'Заказать' ({entry_point})"):
            if entry_point == "top":
                main_page.click_order_button_top()
            else:
                # Прокручиваем до нижней кнопки перед кликом
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)  # Небольшая задержка для прокрутки
                main_page.click_order_button_bottom()

        with allure.step("Заполняем первую страницу заказа"):
            order_page.fill_first_page(**user_data)

        with allure.step("Заполняем вторую страницу заказа"):
            order_page.fill_second_page(**order_data)

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
            WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
            new_window = [window for window in driver.window_handles if window != current_window][0]

        with allure.step("Переключаемся на новую вкладку"):
            driver.switch_to.window(new_window)

        with allure.step("Ожидаем загрузки Дзена"):
            # Ожидаем появления элемента, характерного для Дзена
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located(("css selector", ".dzen-desktop__card"))
            )

        with allure.step("Проверяем URL"):
            assert "dzen.ru" in driver.current_url, \
                f"URL {driver.current_url} не содержит 'dzen.ru'"