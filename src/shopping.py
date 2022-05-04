class ShoppingCart:
    products_tax = {
        "regular_tax":{
            "products":["music cd","bottle of perfume","imported bottle of perfume"],
            "amount":0.1
        }
    }

    def __init__(self,carts=[]):
        self.carts = []

    def add_product(self,qty,product,price):
        try:
            qty = int(qty)
            price = float(price)
            p = (qty,product,price)
            self.carts.append(p)
        except:
            return