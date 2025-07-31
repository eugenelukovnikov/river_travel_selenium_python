from ..settings import *
from ..pages.base_page import BasePage
from ..utils.locators import *


class ServicePage(BasePage): 
    
     SHIP_PAGE_URL = "https://river-travel.ru/services/svadba-teplohode/"

     def __init__(self, driver, url=SHIP_PAGE_URL):
         super().__init__(driver, url)
    # def __init__(self, *args, **kwargs):
    #     super(MainPage, self).__init__(*args, **kwargs)

     def click_submit_calculator_form_on_service_page(self):
          self.driver.find_element(*CalculatorFormLocators.SERVICE_AND_SHIP_PAGE_CALCULATOR_SUBMIT_BUTTON).click() 
    

     def click_get_price_estimate_button_on_service_page(self):
          self.driver.find_element(*GetPriceEstimateFormLocators.SERVICE_PAGE_GET_PRICE_ESTIMATE_BUTTON).click()