class ProductOverview:
    def __init__(self, image=None, name=None, qty=None, price=None):
        self.image = image
        self.name = name
        self.price = price
        self.qty = qty

    def __repr__(self):
        return "ProductOverview({}, {}, {})".format(self.name, self.qty, self.price)
