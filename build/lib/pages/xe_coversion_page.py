from selenium.webdriver.common.by import By

from elements.element_factory import ElementFactory
from .base_page import XeBasePage


class XeConversionPage(XeBasePage):
    def __init__(self, context):
        super().__int__(context)
        self.from_curr_dropdown = ElementFactory(By.XPATH, '//*[@id="midmarketFromCurrency"]', context)
        self.to_curr_dropdown = ElementFactory(By.XPATH, '//*[@id="midmarketToCurrency"]', context)
        self.dropdown_val=ElementFactory(By.XPATH,"//li/div[text()='{}']", context)
        self.convert_btn = ElementFactory(By.XPATH, '//button[text()="Convert"]', context)

    def select_from_currency(self,from_curr):
        self.from_curr_dropdown.element().send_keys(from_curr)


    def select_to_currency(self,to_curr):
        self.to_curr_dropdown.element().send_keys(to_curr)

    def click_convert_btn(self):
        self.convert_btn.element().click()
