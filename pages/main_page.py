from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    # Локаторы
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[contains(text(), 'Заказать')])[2]")
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")

    # Вопросы
    QUESTION_LOCATOR = "//div[@id='accordion__heading-{}']"
    ANSWER_LOCATOR = "//div[@id='accordion__panel-{}']/p"

    def accept_cookies(self):
        self.click_element(self.COOKIE_BUTTON)

    def click_order_button_top(self):
        self.click_element(self.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.click_element(self.ORDER_BUTTON_BOTTOM)

    def click_question(self, question_id):
        locator = (By.XPATH, self.QUESTION_LOCATOR.format(question_id))
        self.click_element(locator)

    def get_answer_text(self, question_id):
        locator = (By.XPATH, self.ANSWER_LOCATOR.format(question_id))
        return self.find_element(locator).text

    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)