from .element import Element


class ElementFactory:
    def __init__(self,selector,locator, context):
        self.selector = selector
        self.locator = locator
        self.context = context

    def element(self):
        return Element(self.selector, self.locator, self.context)

    def element_with_parameters(self, *args):
        return Element(self.selector, self.locator.format(*args), self.context)