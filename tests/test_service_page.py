from ..settings import *
from ..pages.service_page import ServicePage

@allure.title("Проверка работоспособности кнопки и формы 'Получить расчет' на странице услуги.")
def test_get_price_estimate_form_on_service_page(driver):

    page = ServicePage(driver)
    page.open()
    page.click_get_price_estimate_button_on_service_page()
    page.fill_and_send_get_price_estimate_form(date = fake.future_date(end_date='+10d'), supply_type = 'Банкет', guests_amount = 5, hours = 5, last_name = fake.last_name(), phone = fake.phone_number(), communication_method= 'Telegram')
    page.should_be_result_of_sending()

@allure.title("Проверка работоспособности формы 'Калькулятор аренды теплохода' на странице услуги. Позитив.")
def test_calculator_form_result_on_service_page_positive(driver):

    page = ServicePage(driver)
    page.open()
    page.fill_calculator_form(date = fake.future_date(end_date='+10d'), supply_type = 'Банкет', guests_amount = 5, hours = 5)
    page.click_submit_calculator_form_on_service_page()
    page.should_be_ship_count_in_calculator_result()

@allure.title("Проверка работоспособности формы 'Калькулятор аренды теплохода' на странице услуги. Негатив.")
def test_calculator_form_result_on_service_page_negative(driver):

    page = ServicePage(driver)
    page.open()
    page.fill_calculator_form(date = fake.future_date(end_date='+10d'), supply_type = 'Банкет', guests_amount = 999, hours = 999)
    page.click_submit_calculator_form_on_service_page()
    page.should_be_alert_in_calculator_result()

@allure.title("Проверка работоспособности кнопки 'Забронировать' в форме 'Калькулятор аренды теплохода' на странице услуги.")
def test_calculator_form_order_button_on_service_page(driver):

    page = ServicePage(driver)
    page.open()
    page.click_order_form_button_on_calculator()
    page.fill_and_send_order_form(last_name = fake.last_name(), phone = fake.phone_number())
    page.should_be_result_of_sending()

@allure.title("Проверка работоспособности кнопки 'Заказать' и ее формы в блоке 'Популярные теплоходы' на странице услуги.")
def test_order_form_in_ships_block_on_service_page(driver):

    page = ServicePage(driver)
    page.open()
    page.click_on_order_button_in_ships_block()
    page.fill_and_send_order_form(last_name = fake.last_name(), phone = fake.phone_number())
    page.should_be_result_of_sending()