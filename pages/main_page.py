from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    # Локаторы (ИЗМЕНЕНО: улучшены локаторы кнопок)
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")

    # Вопросы
    QUESTION_LOCATOR = (By.XPATH, "//div[@id='accordion__heading-{}']")
    ANSWER_LOCATOR = (By.XPATH, "//div[@id='accordion__panel-{}']/p")

    # Главный заголовок
    MAIN_HEADER = (By.XPATH, "//div[contains(@class, 'Home_Header')]")

    def accept_cookies(self):
        self.click_element(self.COOKIE_BUTTON)

    def click_order_button_top(self):
        self.click_element(self.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.click_element(self.ORDER_BUTTON_BOTTOM)

    def scroll_to_bottom_button(self):
        self.scroll_to_element(self.ORDER_BUTTON_BOTTOM)
        self.wait_for_element_clickable(self.ORDER_BUTTON_BOTTOM)

    def click_question(self, question_id):
        locator = (self.QUESTION_LOCATOR[0],
                   self.QUESTION_LOCATOR[1].format(question_id))
        self.click_element(locator)

    def get_answer_text(self, question_id):
        locator = (self.ANSWER_LOCATOR[0],
                   self.ANSWER_LOCATOR[1].format(question_id))
        return self.find_element(locator).text

    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)

    # ДОБАВЛЕНО: Метод для ожидания элемента Дзена
    def wait_for_dzen_loaded(self):
        self.wait_for_element_visible((By.CSS_SELECTOR, "div.dzen-desktop"), timeout=15)

    def wait_for_page_load(self):
        self.wait_for_element_visible(self.MAIN_HEADER, message="Главная страница не загрузилась")

    def is_main_page_loaded(self):
        try:
            self.find_element(self.MAIN_HEADER, time=5)
            return True
        except:
            return False