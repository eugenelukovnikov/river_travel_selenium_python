from ..settings import *
from ..pages.main_page import MainPage


def test_guest_should_see_calculator_link_in_header(driver):

    page = MainPage(driver)
    page.open()
    page.should_be_calculator_link()


def test_sending_call_me_button_in_header(driver):

    page = MainPage(driver)
    page.open()
    page.should_be_call_me_button_in_header()
    page.fill_and_send_header_call_me(last_name = fake.last_name(), phone = fake.phone_number())
    page.should_be_result_of_sending()


def test_sending_call_me_button_in_footer(driver):

    page = MainPage(driver)
    page.open()
    page.should_be_call_me_button_in_footer()
    page.fill_and_send_footer_call_me(last_name = fake.last_name(), phone = fake.phone_number())
    page.should_be_result_of_sending()


def test_calculator_form_on_main_page_positive(driver):

    page = MainPage(driver)
    page.open()
    page.fill_calculator_form(date = fake.future_date(end_date='+10d'), supply_type = 'Банкет', guests_amount = 5, hours = 5)
    page.click_submit_calculator_form_on_main_page()
    page.should_be_ship_count_in_calculator_result()


def test_calculator_form_on_main_page_negative(driver):

    page = MainPage(driver)
    page.open()
    page.fill_calculator_form(date = fake.future_date(end_date='+10d'), supply_type = 'Банкет', guests_amount = 999, hours = 999)
    page.click_submit_calculator_form_on_main_page()
    page.should_be_alert_in_calculator_result()


def test_calculator_form_order_button_on_main_page(driver):

    page = MainPage(driver)
    page.open()
    page.click_order_form_button_on_calculator()
    page.fill_and_send_order_form(last_name = fake.last_name(), phone = fake.phone_number())
    page.should_be_result_of_sending()


def test_get_price_estimate_form(driver):

    page = MainPage(driver)
    page.open()
    page.click_get_price_estimate_button_on_main_page()
    page.fill_and_send_get_price_estimate_form(date = fake.future_date(end_date='+10d'), supply_type = 'Банкет', guests_amount = 5, hours = 5, last_name = fake.last_name(), phone = fake.phone_number(), communication_method= 'Telegram')
    page.should_be_result_of_sending()


def test_cost_calculation_form_on_main_page(driver):

    page = MainPage(driver)
    page.open()
    page.fill_and_send_cost_calculation_form(date = fake.future_date(end_date='+10d'), supply_type = 'Банкет', guests_amount = 5, hours = 5, last_name = fake.last_name(), phone = fake.phone_number(), communication_method= 'Telegram')
    page.should_be_result_of_sending()


def test_selection_ship_form_on_main_page(driver):

    page = MainPage(driver)
    page.open()
    page.click_selection_of_ship_button_on_main_page()
    page.fill_and_send_selection_ship_form_on_main_page(guests_amount = 'До 30 человек', rent_price = 'до 15000 руб', region = 'Московская область')
    
    page.check_current_url_matches_required(required_url='https://river-travel.ru/ship/?_sft_category=030-050&_sfm_rent=0+15000&_sfm_region=%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C')