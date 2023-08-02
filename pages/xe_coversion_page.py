import time

from selenium.webdriver.common.by import By

from elements.element_factory import ElementFactory
from .base_page import XeBasePage


class XeConversionPage(XeBasePage):
    def __init__(self, context):
        super().__int__(context)
        self.from_curr_dropdown = ElementFactory(By.XPATH, '//*[@id="midmarketFromCurrency"]', context)
        self.to_curr_dropdown = ElementFactory(By.XPATH, '//*[@id="midmarketToCurrency"]', context)
        self.option_from_dropdown=ElementFactory(By.XPATH,"//li/div[contains(text(),'{}')]",context)
        self.amount_field=ElementFactory(By.XPATH,'//*[@id="amount"]', context)
        self.accept_cookies_btn = ElementFactory(By.XPATH, '//button[text()="Accept"]', context)
        self.convert_btn = ElementFactory(By.XPATH, '//button[text()="Convert"]', context)
        self.modal_parent_element=ElementFactory(By.XPATH,"//div[contains(@aria-label, 'Have you tried our money transfer service?')]",context)
        self.notification_modal_element=ElementFactory(By.XPATH,"//div[contains(@aria-label, 'Notification')]",context)
        self.conversion_result_page_from_currency= ElementFactory(By.XPATH,"//*[contains(@class, 'result__ConvertedText')]",context)
        self.conversion_result_page_to_currency= ElementFactory(By.XPATH,"//*[contains(@class, 'result__BigRate')]",context)

    def accept_cookies(self):
        self.accept_cookies_btn.element().click()

    def close_modal(self):
        self.modal_parent_element.element().remove_element()

    def select_from_currency(self,from_curr):
        self.from_curr_dropdown.element().click()
        self.option_from_dropdown.element_with_parameters(from_curr).click()

    def select_to_currency(self,to_curr):
        self.to_curr_dropdown.element().click()
        self.option_from_dropdown.element_with_parameters(to_curr).click()

    def enter_amount(self,amount):
        self.amount_field.element().send_keys(amount)

    def click_convert_btn(self):
        if self.notification_modal_element.element().is_element_visible():
            self.notification_modal_element.element().remove_element()
        self.convert_btn.element().click()

    def get_result_text_for_from_currency(self):
        from_currency_text=self.conversion_result_page_from_currency.element().get_text_present_in_element()
        return from_currency_text

    def get_result_text_for_to_currency(self):
        to_currency_text = self.conversion_result_page_to_currency.element().get_text_present_in_element()
        return to_currency_text
