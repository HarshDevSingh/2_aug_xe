import time

from behave import *
from hamcrest import *

CURRENY_NAME_MAPPING = {
    "EUR": "Euros",
    "INR": "Indian Rupees",
    "RUB": "Russian Rubles",
    "AED": "Emirati Dirhams",
}


@step(u'I am on xe.com currency conversion page')
def open_xe(context):
    context.xe_conversion_page.open()


@step(u'I accept cookies')
def accept_cookies(context):
    context.xe_conversion_page.accept_cookies()


@step(u'I close modal')
def close_model(context):
    context.xe_conversion_page.close_modal()


@step(u'I enter {from_amount}')
def accept_cookies(context,from_amount):
    context.from_amount = from_amount
    context.xe_conversion_page.enter_amount(context.from_amount)


@step(u'I select {from_currency} source')
def select_from_currency(context,from_currency):
    context.from_currency = from_currency
    context.xe_conversion_page.select_from_currency(context.from_currency)


@step(u'I select target {to_currency}')
def select_to_currency(context,to_currency):
    context.to_currency = to_currency
    context.xe_conversion_page.select_to_currency(context.to_currency)


@step(u'I submit currency pair to get conversion rate')
def submit_currency_for_conversion(context):
    context.xe_conversion_page.click_convert_btn()


@step('I should see correct data for "form" and "to" currency on conversion result page')
def assert_result_data(context):
    from_currency_text = context.xe_conversion_page.get_result_text_for_from_currency()
    to_currency_text = context.xe_conversion_page.get_result_text_for_to_currency()
    from_currency_text_list = from_currency_text.split()
    assert_that(context.from_amount, is_(equal_to(from_currency_text_list[0].replace(",", ""))))
    get_name_and_amount_list = from_currency_text_list[:-1]
    from_currency_name_on_result_page = ' '.join(get_name_and_amount_list[1:]) if len(
        get_name_and_amount_list) > 2 else \
        get_name_and_amount_list[1]
    assert_that(CURRENY_NAME_MAPPING.get(context.from_currency), is_(equal_to(from_currency_name_on_result_page)))
    to_currency_text_list = to_currency_text.split()
    to_currency_name_on_result_page = ' '.join(to_currency_text_list[1:]) if len(to_currency_text_list) > 2 else \
        to_currency_text_list[1]
    assert_that(CURRENY_NAME_MAPPING.get(context.to_currency), is_(equal_to(to_currency_name_on_result_page)))
