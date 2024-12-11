from estoreproject.productcategory import ProductCategory


class Product:
    def __init__(self, product_id, product_name, price, product_description):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.product_description = product_description
        self.electronics = ProductCategory.ELECTRONICS
        self.groceries = ProductCategory.GROCERIES
        self.utensils = ProductCategory.UTENSILS
        self.clothing = ProductCategory.CLOTHING