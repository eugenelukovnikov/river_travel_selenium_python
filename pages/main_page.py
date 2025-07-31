from ..settings import *
from ..pages.base_page import BasePage
from ..utils.locators import *


class MainPage(BasePage): 
    
     MAIN_PAGE_URL = "https://river-travel.ru/"

     def __init__(self, driver, url=MAIN_PAGE_URL):
         super().__init__(driver, url)
    # def __init__(self, *args, **kwargs):
    #     super(MainPage, self).__init__(*args, **kwargs)

     def click_submit_calculator_form_on_main_page(self):
          self.driver.find_element(*CalculatorFormLocators.MAIN_PAGE_CALCULATOR_SUBMIT_BUTTON).click() 

     def click_get_price_estimate_button_on_main_page(self):
          self.driver.find_element(*GetPriceEstimateFormLocators.MAIN_PAGE_GET_PRICE_ESTIMATE_BUTTON).click()

     def click_selection_of_ship_button_on_main_page(self):
          
          self.driver.find_element(*SelectionOfShipFormLocators.SELECTION_SHIP_BUTTON).click()

     def fill_and_send_selection_ship_form_on_main_page(self, guests_amount, rent_price, region):
  
          guests_amount_select = Select(self.driver.find_element(*SelectionOfShipFormLocators.SELECTION_SHIP_FORM_GUESTS_AMOUNT))
          guests_amount_select.select_by_visible_text(guests_amount)

          rent_price_select = Select(self.driver.find_element(*SelectionOfShipFormLocators.SELECTION_SHIP_FORM_RENT_PRICE))
          rent_price_select.select_by_visible_text(rent_price)
          
          region_select = Select(self.driver.find_element(*SelectionOfShipFormLocators.SELECTION_SHIP_FORM_REGION))
          region_select.select_by_visible_text(region)

          self.driver.find_element(*SelectionOfShipFormLocators.SELECTION_SHIP_FORM_SUBMIT_BUTTON).click()
