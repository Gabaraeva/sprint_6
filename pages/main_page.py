from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    # Локаторы
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[contains(text(), 'Заказать')])[2]")
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")

    # Вопросы
    QUESTION_LOCATOR = (By.XPATH, "//div[@id='accordion__heading-{}']")
    ANSWER_LOCATOR = (By.XPATH, "//div[@id='accordion__panel-{}']/p")

    # Главный заголовок для проверки загрузки
    MAIN_HEADER = (By.XPATH, "//div[contains(@class, 'Home_Header')]")

    def accept_cookies(self):
        """Принять куки"""
        self.click_element(self.COOKIE_BUTTON)

    def click_order_button_top(self):
        """Клик по верхней кнопке 'Заказать'"""
        self.click_element(self.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        """Клик по нижней кнопке 'Заказать'"""
        self.click_element(self.ORDER_BUTTON_BOTTOM)

    def scroll_to_bottom_button(self):
        """Прокрутить к нижней кнопке 'Заказать'"""
        self.scroll_to_element(self.ORDER_BUTTON_BOTTOM)
        self.wait_for_element_clickable(self.ORDER_BUTTON_BOTTOM)

    def click_question(self, question_id):
        """Клик по вопросу с указанным ID"""
        locator = (self.QUESTION_LOCATOR[0],
                   self.QUESTION_LOCATOR[1].format(question_id))
        self.click_element(locator)

    def get_answer_text(self, question_id):
        """Получить текст ответа на вопрос"""
        locator = (self.ANSWER_LOCATOR[0],
                   self.ANSWER_LOCATOR[1].format(question_id))
        return self.find_element(locator).text

    def click_scooter_logo(self):
        """Клик по логотипу Самоката"""
        self.click_element(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        """Клик по логотипу Яндекса"""
        self.click_element(self.YANDEX_LOGO)

    def wait_for_page_load(self):
        """Ожидание загрузки главной страницы"""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.MAIN_HEADER),
            message="Главная страница не загрузилась"
        )

    def is_main_page_loaded(self):
        """Проверка загрузки главной страницы"""
        try:
            self.find_element(self.MAIN_HEADER, time=5)
            return True
        except:
            return False