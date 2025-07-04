from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import Select


class OrderPage(BasePage):
    # Локаторы для первой страницы заказа
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_ITEM = (By.XPATH, "//div[text()='{}']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Локаторы для второй страницы заказа
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[text()='* Срок аренды']")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[text()='{}']")
    COLOR_CHECKBOX = (By.ID, "{}")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")

    def fill_first_page(self, name, last_name, address, metro_station, phone):
        self.find_element(self.NAME_INPUT).send_keys(name)
        self.find_element(self.LAST_NAME_INPUT).send_keys(last_name)
        self.find_element(self.ADDRESS_INPUT).send_keys(address)
        self.click_element(self.METRO_STATION_INPUT)

        # Выбор станции метро
        metro_locator = (self.METRO_STATION_ITEM[0], self.METRO_STATION_ITEM[1].format(metro_station))
        self.click_element(metro_locator)

        self.find_element(self.PHONE_INPUT).send_keys(phone)
        self.click_element(self.NEXT_BUTTON)

    def fill_second_page(self, date, period, color, comment):
        self.find_element(self.DATE_INPUT).send_keys(date)
        self.click_element(self.RENTAL_PERIOD_DROPDOWN)

        # Выбор срока аренды
        period_locator = (self.RENTAL_PERIOD_OPTION[0], self.RENTAL_PERIOD_OPTION[1].format(period))
        self.click_element(period_locator)

        # Выбор цвета
        if color:
            color_locator = (By.ID, self.COLOR_CHECKBOX[1].format(color))
            self.click_element(color_locator)

        self.find_element(self.COMMENT_INPUT).send_keys(comment)
        self.click_element(self.ORDER_BUTTON)
        self.click_element(self.CONFIRM_BUTTON)

    def is_order_successful(self):
        return self.find_element(self.SUCCESS_MESSAGE).is_displayed()