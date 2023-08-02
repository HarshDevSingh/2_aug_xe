import time

from behave import *


@given(u'I open xe.com')
def open_xe(context):
    context.xe_conversion_page.open()
    time.sleep(5)
