from ..settings import *
from ..pages.ship_page import ShipPage


def test_calculator_form_result_on_ship_page_positive(driver):

    page = ShipPage(driver)
    page.open()
    page.fill_calculator_form(date = fake.future_date(end_date='+10d'), supply_type = 'Банкет', guests_amount = 5, hours = 5)
    page.click_submit_calculator_form_on_ship_page()
    page.should_be_ship_count_in_calculator_result()


def test_calculator_form_result_on_ship_page_negative(driver):

    page = ShipPage(driver)
    page.open()
    page.fill_calculator_form(date = fake.future_date(end_date='+10d'), supply_type = 'Банкет', guests_amount = 999, hours = 999)
    page.click_submit_calculator_form_on_ship_page()
    page.should_be_alert_in_calculator_result()


def test_calculator_form_order_button_on_ship_page(driver):

    page = ShipPage(driver)
    page.open()
    page.click_order_form_button_on_calculator()
    page.fill_and_send_order_form(last_name = fake.last_name(), phone = fake.phone_number())
    page.should_be_result_of_sending()


def test_get_consultation_form_on_ship_page(driver):

    page = ShipPage(driver)
    page.open()
    page.click_get_consultation_form_button_on_ship_page()
    page.should_be_ship_name_in_get_consultation_form()
    page.fill_and_send_get_consultation_form(phone = fake.phone_number())
    page.should_be_result_for_get_consultation_form()


def test_order_form_on_ship_page(driver):

    page = ShipPage(driver)
    page.open()
    page.click_order_form_button_on_ship_page()
    page.fill_and_send_order_form(last_name = fake.last_name(), phone = fake.phone_number())
    page.should_be_result_of_sending()
    

def test_order_form_in_ships_block_on_ship_page(driver):

    page = ShipPage(driver)
    page.open()
    page.click_on_order_button_in_ships_block()
    page.fill_and_send_order_form(last_name = fake.last_name(), phone = fake.phone_number())
    page.should_be_result_of_sending()