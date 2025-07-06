import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import URLs  # Импортируем URL из конфигурационного файла


@pytest.fixture(scope="function")
def driver():
    # Настройка драйвера Firefox
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()

    # Открываем тестовый сайт, используя константу из config.py
    driver.get(URLs.MAIN_PAGE)

    # Ожидаем загрузки страницы (явное ожидание)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(("xpath", "//div[contains(@class, 'Home_Header')]"))
    )

    yield driver

    # Закрываем браузер после теста
    driver.quit()


# Хук для создания скриншотов при падении тестов
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        # Получаем драйвер из фикстуры
        driver = item.funcargs.get('driver')
        if driver:
            # Прикрепляем скриншот к Allure-отчёту
            allure.attach(
                driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )