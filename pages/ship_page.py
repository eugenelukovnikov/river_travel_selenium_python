from ..settings import *
from ..pages.base_page import BasePage
from ..utils.locators import *


class ShipPage(BasePage): 
    
     SHIP_PAGE_URL = "https://river-travel.ru/ship/teplohod-bogema/"

     def __init__(self, driver, url=SHIP_PAGE_URL):
         super().__init__(driver, url)
    # def __init__(self, *args, **kwargs):
    #     super(MainPage, self).__init__(*args, **kwargs)

     def click_submit_calculator_form_on_ship_page(self):
          self.driver.find_element(*CalculatorFormLocators.SERVICE_AND_SHIP_PAGE_CALCULATOR_SUBMIT_BUTTON).click() 
    

     def click_order_form_button_on_ship_page(self):
          self.driver.find_element(*OrderFormLocators.SHIP_PAGE_ORDER_SHIP_FORM_BUTTON).click()


     def click_get_consultation_form_button_on_ship_page(self):
          self.driver.find_element(*GetConsultationFormLocators.GET_CONSULTATION_FORM_BUTTON).click()