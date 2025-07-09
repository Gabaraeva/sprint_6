import pytest
import allure
from pages.main_page import MainPage
from test_data import QuestionsAnswers  # Импортируем ожидаемые ответы


@allure.feature("Тесты раздела 'Вопросы о важном'")
class TestQuestions:

    @allure.title("Проверка ответа на вопрос №{question_id}")
    @pytest.mark.parametrize("question_id", list(range(8)))
    def test_question_answer(self, driver, question_id):
        main_page = MainPage(driver)

        with allure.step("Принимаем куки"):
            main_page.accept_cookies()

        with allure.step(f"Нажимаем на вопрос №{question_id}"):
            main_page.click_question(question_id)

        with allure.step("Получаем текст ответа"):
            actual_answer = main_page.get_answer_text(question_id)

        with allure.step("Сравниваем с ожидаемым ответом"):
            expected_answer = QuestionsAnswers.ANSWERS[question_id]
            assert actual_answer == expected_answer, \
                f"Ожидался ответ: '{expected_answer}'\nПолучен ответ: '{actual_answer}'"