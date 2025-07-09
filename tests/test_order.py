import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from test_data import OrderData


@allure.feature("Тесты заказа самоката")
class TestOrder:

    @allure.title("Тест заказа самоката через верхнюю кнопку")
    def test_order_scooter_top_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.accept_cookies()
        main_page.click_order_button_top()
        order_page.fill_first_page(**OrderData.TOP_ORDER['user_data'])
        order_page.fill_second_page(**OrderData.TOP_ORDER['order_data'])
        assert order_page.is_order_successful(), "Заказ не был успешно оформлен"

    @allure.title("Тест заказа самоката через нижнюю кнопку")
    def test_order_scooter_bottom_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.accept_cookies()
        main_page.scroll_to_bottom_button()
        main_page.click_order_button_bottom()
        order_page.fill_first_page(**OrderData.BOTTOM_ORDER['user_data'])
        order_page.fill_second_page(**OrderData.BOTTOM_ORDER['order_data'])
        assert order_page.is_order_successful(), "Заказ не был успешно оформлен"

    @allure.title("Проверка перехода по логотипу Самоката")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_scooter_logo()

        # ИЗМЕНЕНО: Используем методы Page Object
        assert main_page.get_current_url() == "https://qa-scooter.praktikum-services.ru/", \
            f"Ожидался URL https://qa-scooter.praktikum-services.ru/, получен {main_page.get_current_url()}"

    @allure.title("Проверка перехода по логотипу Яндекса")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()

        # ИЗМЕНЕНО: Полностью убраны прямые вызовы driver
        current_window = main_page.get_current_window_handle()
        main_page.click_yandex_logo()
        main_page.switch_to_new_window(current_window)
        main_page.wait_for_dzen_loaded()

        # ИЗМЕНЕНО: Используем метод Page Object
        assert main_page.is_url_contains("dzen.ru"), \
            f"URL {main_page.get_current_url()} не содержит 'dzen.ru'"