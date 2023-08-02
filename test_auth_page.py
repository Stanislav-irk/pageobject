from pages.auth_page import AuthPage
import time


def test_auth_page(driver):
    page = AuthPage(driver)
    page.enter_email("stanislav-irk@bk.ru")
    page.enter_pass('Taisia-28.11')
    page.btn_click()

    # знак != или == будет зависеть от того, верные или неверные данные мы вводим
    assert page.get_relative_link() == '/all_pets', 'login error'

    time.sleep(5)  # задержка для учебных целей
