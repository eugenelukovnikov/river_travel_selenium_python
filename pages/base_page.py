from ..settings import *
from ..utils.locators import *


class BasePage():
    
    def __init__(self, driver, url, timeout=5):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)

    def go_to_calculator_page(self):
        link = self.driver.find_element(*BasePageLocators.HEADER_CALCULATOR_LINK)
        link.click()

    # def is_element_present(self, how, what):
    #     try:
    #         self.driver.find_element(how, what)
    #     except (NoSuchElementException):
    #         return False
    #     return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    
    def is_element_present(self, how, what, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True


    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException).until_not(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
   
    def should_be_calculator_link(self):
        assert self.is_element_present(*BasePageLocators.HEADER_CALCULATOR_LINK), "Ссылка на калькулятор в шапке не найдена"

    def should_be_call_me_button_in_header(self):
        assert self.is_element_present(*BasePageLocators.HEADER_CALL_ME_BUTTON), "Кнопка Перезвоните мне в шапке не найдена"

    def should_be_call_me_button_in_footer(self):
        assert self.is_element_present(*BasePageLocators.FOOTER_CALL_ME_BUTTON), "Кнопка онлайн-заявка в подвале не найдена"       

    def should_be_search_field_in_header(self):
        assert self.is_element_present(*BasePageLocators.HEADER_SEARCH), "Не найдено поле Поиска в шапке"  

    def should_be_calculator_order_button_on_main_and_ship_pages(self):
        assert self.is_element_present(*OrderFormLocators.CALCULATOR_ORDER_BUTTON), "Должна быть кнопка Забронировать в калькуляторе"

    def should_be_ship_order_button_on_ship_pages_in_popular_ships_block(self):
        assert self.is_element_present(*OrderFormLocators.FIRST_SHIP_ORDER_BUTTON), "Должна быть кнопка Заказать у теплоходов в блоке Теплоходы"

    def should_be_ship_order_button_on_ship_pages(self):
        assert self.is_element_present(*OrderFormLocators.SHIP_PAGE_ORDER_SHIP_FORM_BUTTON), "Должна быть кнопка Забронировать на странице теплоходов"

    def should_be_get_price_estimate_button_on_main_page(self):
        assert self.is_element_present(*GetPriceEstimateFormLocators.MAIN_PAGE_GET_PRICE_ESTIMATE_BUTTON), "Должна быть кнопка Получить расчет на главной на первом экране"

    def should_be_get_price_estimate_button_on_service_page(self):
        assert self.is_element_present(*GetPriceEstimateFormLocators.SERVICE_PAGE_GET_PRICE_ESTIMATE_BUTTON), "Должна быть кнопка Узнать стоимость на услуге в одноименном блоке"

    def should_be_selection_ship_button_on_main_page(self):
        assert self.is_element_present(*SelectionOfShipFormLocators.SELECTION_SHIP_BUTTON), "Должна быть кнопка Подобрать теплоход на главной"
   
    def should_be_cost_calculation_form_on_main_page(self):
        assert self.is_element_present(*CostCalculationFormLocators.FORM_COST_EVENT), "Должна быть форма Расчёт стоимости мероприятия на главной"

    def should_be_get_consultation_button_on_ship_page(self):
        assert self.is_element_present(*GetConsultationFormLocators.GET_CONSULTATION_FORM_BUTTON), "Должна быть кнопка Получить консультацию на страницах теплоходов"


    def fill_and_send_header_call_me(self, last_name, phone):
        
        self.driver.find_element(*BasePageLocators.HEADER_CALL_ME_BUTTON).click() 

        self.driver.find_element(*BasePageLocators.HEADER_CALL_ME_FIO).send_keys(last_name) 
        self.driver.find_element(*BasePageLocators.HEADER_CALL_ME_PHONE).send_keys(phone) 

        self.driver.find_element(*BasePageLocators.HEADER_CALL_ME_SUBMIT_BUTTON).click() 
    
    def fill_and_send_footer_call_me(self, last_name, phone):
        
        self.driver.find_element(*BasePageLocators.FOOTER_CALL_ME_BUTTON).click() 

        self.driver.find_element(*BasePageLocators.FOOTER_CALL_ME_FIO).send_keys(last_name) 
        self.driver.find_element(*BasePageLocators.FOOTER_CALL_ME_PHONE).send_keys(phone) 

        self.driver.find_element(*BasePageLocators.FOOTER_CALL_ME_SUBMIT_BUTTON).click()

    def should_be_result_of_sending(self):
        
        assert self.is_element_present(*BasePageLocators.RESULT_OF_SENDING), "Нет окна с результатом отправки формы"

    def fill_calculator_form(self, date, supply_type, guests_amount, hours):

        date_field = self.driver.find_element(*CalculatorFormLocators.CALCULATOR_DATE)
        self.driver.execute_script("arguments[0].removeAttribute('readonly')", date_field)
        date_str = date.strftime('%d.%m.%Y')
        date_field.send_keys(date_str) 
        
        select = Select(self.driver.find_element(*CalculatorFormLocators.CALCULATOR_SUPPLY_TYPE))
        select.select_by_visible_text(supply_type)
        
        self.driver.find_element(*CalculatorFormLocators.CALCULATOR_GUESTS_AMOUNT).send_keys(guests_amount) 
        
        self.driver.find_element(*CalculatorFormLocators.CALCULATOR_HOURS).send_keys(hours) 


    def should_be_ship_count_in_calculator_result(self):
        assert self.is_element_present(*CalculatorFormLocators.CALCULATOR_RESULT_COUNT_TEXT ), "Число теплоходов не указано"  

    def should_be_alert_in_calculator_result(self):
        assert self.is_element_present(*CalculatorFormLocators.CALCULATOR_RESULT_ALERT), "Алерт с ошибкой не появился"  

    def fill_and_send_order_form(self, last_name, phone):

        self.driver.find_element(*OrderFormLocators.ORDER_FORM_FIO_FIELD).send_keys(last_name) 
        self.driver.find_element(*OrderFormLocators.ORDER_FORM_PHONE_FIELD).send_keys(phone) 

        self.driver.find_element(*OrderFormLocators.ORDER_FORM_SUBMIT_BUTTON).click()
    
    def fill_and_send_get_price_estimate_form(self, date, guests_amount, hours, supply_type, communication_method, last_name, phone):

        date_field = self.driver.find_element(*GetPriceEstimateFormLocators.GET_PRICE_ESTIMATE_FORM_DATE_FIELD)
        date_str = date.strftime('%d.%m.%Y')
        date_field.send_keys(date_str)
        
        self.driver.find_element(*GetPriceEstimateFormLocators.GET_PRICE_ESTIMATE_FORM_GUESTS_AMOUNT).send_keys(guests_amount)
        
        self.driver.find_element(*GetPriceEstimateFormLocators.GET_PRICE_ESTIMATE_FORM_HOURS).send_keys(hours)
        
        supply_select = Select(self.driver.find_element(*GetPriceEstimateFormLocators.GET_PRICE_ESTIMATE_FORM_SUPPLY_TYPE))
        supply_select.select_by_visible_text(supply_type)
        
        communication_method_select = Select(self.driver.find_element(*GetPriceEstimateFormLocators.GET_PRICE_ESTIMATE_FORM_COMMUNICATION_METHOD))
        communication_method_select.select_by_visible_text(communication_method)
        
        self.driver.find_element(*GetPriceEstimateFormLocators.GET_PRICE_ESTIMATE_FORM_FIO_FIELD).send_keys(last_name)
        
        self.driver.find_element(*GetPriceEstimateFormLocators.GET_PRICE_ESTIMATE_FORM_PHONE_FIELD).send_keys(phone)
        
        self.driver.find_element(*GetPriceEstimateFormLocators.GET_PRICE_ESTIMATE_FORM_SUBMIT_BUTTON).click()


    def fill_and_send_cost_calculation_form(self, date, guests_amount, hours, supply_type, communication_method, last_name, phone):

        date_field = self.driver.find_element(*CostCalculationFormLocators.COST_EVENT_DATE_FIELD)
        date_str = date.strftime('%d.%m.%Y')
        date_field.send_keys(date_str)
       
        self.driver.find_element(*CostCalculationFormLocators.COST_EVENT_FORM_GUESTS_AMOUNT).send_keys(guests_amount)
        
        self.driver.find_element(*CostCalculationFormLocators.COST_EVENT_FORM_HOURS).send_keys(hours)
        
        supply_select = Select(self.driver.find_element(*CostCalculationFormLocators.COST_EVENT_FORM_SUPPLY_TYPE))
        supply_select.select_by_visible_text(supply_type)
        
        communication_method_select = Select(self.driver.find_element(*CostCalculationFormLocators.COST_EVENT_FORM_COMMUNICATION_METHOD))
        communication_method_select.select_by_visible_text(communication_method)
        
        self.driver.find_element(*CostCalculationFormLocators.COST_EVENT_FORM_FIO_FIELD).send_keys(last_name)
        
        self.driver.find_element(*CostCalculationFormLocators.COST_EVENT_FORM_PHONE_FIELD).send_keys(phone)

        self.driver.find_element(*CostCalculationFormLocators.COST_EVENT_FORM_SUBMIT_BUTTON).click()

    def fill_and_send_get_consultation_form(self, phone):
        
        self.driver.find_element(*GetConsultationFormLocators.GET_CONSULTATION_FORM_PHONE_FIELD).send_keys(phone)

        self.driver.find_element(*GetConsultationFormLocators.GET_CONSULTATION_FORM_SUBMIT_BUTTON).click()

    def should_be_ship_name_in_get_consultation_form(self):
        
        assert self.is_element_present(*GetConsultationFormLocators.GET_CONSULTATION_FORM_SHIP_NAME), "Название теплохода отсутствует в форме"

    
    def should_be_result_for_get_consultation_form(self):

        assert self.is_element_present(*GetConsultationFormLocators.GET_CONSULTATION_SENDING_POSITIVE_RESULT), "Не появилось сообщение об отправке"
    

    def click_on_order_button_in_ships_block(self):

        self.driver.find_element(*OrderFormLocators.FIRST_SHIP_ORDER_BUTTON).click()

    def click_order_form_button_on_calculator(self):
        self.driver.find_element(*OrderFormLocators.CALCULATOR_ORDER_BUTTON).click()

    def check_current_url_matches_required(self, required_url):
        assert self.driver.current_url == required_url, f'Урлы не совпали. Сейчас: {self.driver.current_url}, а требуется: {required_url}'