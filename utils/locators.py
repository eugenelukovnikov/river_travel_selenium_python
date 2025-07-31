
class BasePageLocators():

    RESULT_OF_SENDING = ('xpath', "//div[contains(@class,'message fancybox-content')]//p")
    
    ALL_SERVICES_LINKS = ('xpath', "//div[@class='header__desktop']//li[@id='menu-item-416']//a")
    
    ALL_SHIP_CAT_LINKS = ('xpath', "//div[@class='header__desktop']//li[@id='menu-item-52871']//a")

    
    # Форма "CALL_ME_BUTTON / Перезвоните мне" (2 поля и кнопка):

    HEADER_CALL_ME_BUTTON = ('xpath', "//button[contains(@data-src,'callback')]")

    HEADER_CALL_ME_FIO = ('xpath', "//div[@id='callback']//input[@name='FIO']")
    HEADER_CALL_ME_PHONE = ('xpath', "//div[@id='callback']//input[@name='PHONE']")
    HEADER_CALL_ME_SUBMIT_BUTTON = ('xpath', "//div[@id='callback']//button[@type='submit']")

    # Ссылка на Калькулятор:

    HEADER_CALCULATOR_LINK = ('xpath', "//header//a[contains(@href,'/kalkulyator/')]")

    # Поле поиска

    HEADER_SEARCH = ('xpath', "//div[@class='header__menu']//input[contains(@id,'ship_phrase')]")

    # Оставить заявку:

    FOOTER_CALL_ME_BUTTON = ('xpath', "//footer//button[@data-src='order']")
    
    FOOTER_CALL_ME_FIO = ('xpath', "//div[@id='order']//input[@name='FIO']")
    FOOTER_CALL_ME_PHONE = ('xpath', "//div[@id='order']//input[@name='PHONE']")
    FOOTER_CALL_ME_SUBMIT_BUTTON = ('xpath', "//div[@id='order']//button[@type='submit']")


class CalculatorFormLocators():

    # Обязательные поля:

    CALCULATOR_DATE = ('xpath', "//div[@id='calc']//input[@name='date']")
    CALCULATOR_SUPPLY_TYPE = ('xpath', "//div[@id='calc']//select[@name='event']")
    CALCULATOR_GUESTS_AMOUNT = ('xpath', "//div[@id='calc']//input[@name='numpeople']")
    CALCULATOR_HOURS = ('xpath', "//div[@id='calc']//input[@name='numhour']")


    # Отличия кнопок Рассчитать для главной, теплоходов и услуг:

    MAIN_PAGE_CALCULATOR_SUBMIT_BUTTON = ('xpath', "//div[@id='calc']//button[@type='submit']")

    SERVICE_AND_SHIP_PAGE_CALCULATOR_SUBMIT_BUTTON = ('xpath', "//div[@id='calc']//button[@class='btn load']")

    # Результаты формы "Калькулятор аренды теплохода":

    CALCULATOR_RESULT_COUNT_TEXT = ('xpath', "//div[@id='calc']//div[@class='calculator__text']//strong")
    CALCULATOR_RESULT_SHIPS =('xpath', "//div[@id='calc']//div[contains(@class, 'calculator__ship')]")
    CALCULATOR_RESULT_ALERT = ('xpath', "//div[@class='alert alert-warning']")


class OrderFormLocators():

    # Кнопка Заказать / Забронировать и форма Оставить заявку:

    CALCULATOR_ORDER_BUTTON = ('xpath', "//div[@id='calc']//button[@data-src='#order-ship']") # Забронировать в калькуляторе
   
    ALL_SHIPS_ORDER_BUTTONS = ('xpath', "//div[@class='ship-list']//button[@data-src='#order-ship']") # кнопка Заказать в блоке Теплоходы

    FIRST_SHIP_ORDER_BUTTON = ('xpath', "(//div[@class='ship-list']//button[@data-src='#order-ship'])[1]") # кнопка Заказать у первого теплохода в блоке Теплоходы

    SHIP_PAGE_ORDER_SHIP_FORM_BUTTON = ('xpath', "//div[@class='question__wrap']//button[@data-src='#order-ship']") # Забронировать на странице теплоходов

    # Общие для всех поля формы:

    ORDER_FORM_FIO_FIELD = ('xpath', "//div[@id='order-ship']//input[@name='FIO']")
    ORDER_FORM_PHONE_FIELD = ('xpath', "//div[@id='order-ship']//input[@name='PHONE']")
    ORDER_FORM_SUBMIT_BUTTON = ('xpath', "//div[@id='order-ship']//button[@type='submit']")


class GetPriceEstimateFormLocators():

    # Форма "Получить расчет":

    MAIN_PAGE_GET_PRICE_ESTIMATE_BUTTON = ('xpath', "//button[@data-src='calculator']") # На главной на первом экране
    
    SERVICE_PAGE_GET_PRICE_ESTIMATE_BUTTON = ('xpath', "(//div[@class='contacts__form']//button[@data-src='calculator'])[1]") # На услуге в блоке Узнать стоимость

    GET_PRICE_ESTIMATE_FORM_DATE_FIELD = ('xpath', "//div[@id='calculator']//input[@id='calc-date']")
    GET_PRICE_ESTIMATE_FORM_GUESTS_AMOUNT = ('xpath', "//div[@id='calculator']//input[@id='calc-num']")
    GET_PRICE_ESTIMATE_FORM_HOURS = ('xpath', "//div[@id='calculator']//input[@id='calc-hours']")
    GET_PRICE_ESTIMATE_FORM_SUPPLY_TYPE = ('xpath', "//div[@id='calculator']//select[@id='measure-type']")
    GET_PRICE_ESTIMATE_FORM_COMMUNICATION_METHOD = ('xpath', "//div[@id='calculator']//select[@id='kuda-otpravit']")
    GET_PRICE_ESTIMATE_FORM_FIO_FIELD = ('xpath', "//div[@id='calculator']//input[@id='calc-name']")
    GET_PRICE_ESTIMATE_FORM_PHONE_FIELD = ('xpath', "//div[@id='calculator']//input[@id='calc-tel']")
    GET_PRICE_ESTIMATE_FORM_SUBMIT_BUTTON = ('xpath', "//div[@id='calculator']//button[@id='calc-send']")


class SelectionOfShipFormLocators():
    
    # Форма Подбор теплохода - пока на главной:
    
    SELECTION_SHIP_BUTTON = ('xpath', "//button[@data-src='#select-ship']")

    SELECTION_SHIP_FORM_GUESTS_AMOUNT = ('xpath', "//div[@class='select-ship__form']//li[@class='sf-field-category']//select[@class='sf-input-select']")
    SELECTION_SHIP_FORM_RENT_PRICE = ('xpath', "//div[@class='select-ship__form']//li[@class='sf-field-post-meta-rent']//select[@class='sf-input-select']")
    SELECTION_SHIP_FORM_REGION = ('xpath', "//div[@class='select-ship__form']//li[@class='sf-field-post-meta-region']//select[@class='sf-input-select']")
    SELECTION_SHIP_FORM_SUBMIT_BUTTON = ('xpath', "//div[@class='select-ship__form']//li[@class='sf-field-submit']//input[@type='submit']")
    

class CostCalculationFormLocators():

    # Форма "Расчёт стоимости мероприятия" - пока на главной:

    FORM_COST_EVENT = ('xpath', "//section[@class='home-form']")


    COST_EVENT_DATE_FIELD = ('xpath', "//section[@class='home-form']//input[@id='calc-date']")
    COST_EVENT_FORM_GUESTS_AMOUNT = ('xpath', "//section[@class='home-form']//input[@id='calc-num']")
    COST_EVENT_FORM_HOURS = ('xpath', "//section[@class='home-form']//input[@id='calc-hours']")
    COST_EVENT_FORM_SUPPLY_TYPE = ('xpath', "//section[@class='home-form']//select[@id='measure-type']")
    COST_EVENT_FORM_COMMUNICATION_METHOD = ('xpath', "//section[@class='home-form']//select[@id='kuda-otpravit']")
    COST_EVENT_FORM_FIO_FIELD = ('xpath', "//section[@class='home-form']//input[@id='calc-name']")
    COST_EVENT_FORM_PHONE_FIELD = ('xpath', "//section[@class='home-form']//input[@id='calc-tel']")
    COST_EVENT_FORM_SUBMIT_BUTTON = ('xpath', "//section[@class='home-form']//button[@id='calc-send']")


class GetConsultationFormLocators():
    

    # Получить консультацию - форма и кнопка на страницах теплоходов

    GET_CONSULTATION_FORM_BUTTON = ('xpath', "//div[@class='question__wrap']//a[@data-src='#cons-ship']")
    
    GET_CONSULTATION_FORM_SHIP_NAME = ('xpath', "//div[@id='cons-ship']//div[@class='t-center']//div[@class='text']") # для проверки названия теплохода в форме
    
    GET_CONSULTATION_FORM_PHONE_FIELD = ('xpath', "//div[@id='cons-ship']//input[@name='PHONE']")
    
    GET_CONSULTATION_FORM_SUBMIT_BUTTON = ('xpath', "//div[@id='cons-ship']//button[@type='submit']")

    GET_CONSULTATION_SENDING_POSITIVE_RESULT = ('xpath', "//div[@role='alert']")
    
