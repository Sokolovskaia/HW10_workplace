class Product:
    def __init__(
            self,
            name,
            vendor_code,
            size,  # размер
            price,
            number,  # количество
            selling=False  # False - не продан
    ):
        self.name = name
        self.vendor_code = vendor_code
        self.size = size
        self.price = price
        self.number = number
        self.selling = selling


class ProductManager:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def availability(self):
        return list(filter(lambda product: not product.selling, self.items))

    def sales(self):
        return list(filter(lambda product: product.selling, self.items))



