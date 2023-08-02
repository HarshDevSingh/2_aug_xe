from .base_element import BaseElement


class Element(BaseElement):
    def __int__(self, selector,locator, context):
        super().__init__(selector,locator, context)