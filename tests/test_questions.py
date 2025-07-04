import pytest
import allure
from pages.main_page import MainPage


@allure.feature("Тесты раздела 'Вопросы о важном'")
class TestQuestions:
    QUESTIONS_IDS = [0, 1, 2, 3, 4, 5, 6, 7]

    @allure.title("Проверка ответа на вопрос №{question_id}")
    @pytest.mark.parametrize("question_id", QUESTIONS_IDS)
    def test_question_answer(self, driver, question_id):
        main_page = MainPage(driver)
        main_page.accept_cookies()

        with allure.step(f"Нажимаем на вопрос №{question_id}"):
            main_page.click_question(question_id)

        with allure.step("Проверяем, что отображается ответ"):
            answer = main_page.get_answer_text(question_id)
            assert answer != "", f"Ответ на вопрос №{question_id} не отображается"