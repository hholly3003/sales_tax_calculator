class ShoppingCart:
    products_tax = {
        "regular_tax":{
            "products":["music cd","bottle of perfume","imported bottle of perfume"],
            "amount":0.1
        }
    }

    def __init__(self,carts=[]):
        self.carts = []

    # add product to the cart
    def add_product(self,qty,product,price):
        try:
            qty = int(qty)
            price = float(price)
            p = (qty,product,price)
            self.carts.append(p)
        except:
            return
    
    # calculate the sales tax for each product 
    def calculate_sales_tax(self, qty, product, price):
        tax_percentage = self.get_tax_percentage(product)
        sales_tax = round(qty*price*tax_percentage,3)
        sales_tax = self.round_decimals_up(sales_tax)
        return sales_tax

    # calculate the final price for each product inc tax
    def calculate_price(self, qty, product, price):
        sales_tax = self.calculate_sales_tax(qty,product,price)
        product_price = price + sales_tax
        product_price = round(product_price,2)
        return product_price
    
    # get the tax percentage each product need to pay
    def get_tax_percentage(self, product):
        tax_percentage = 0
        if "import" in product:
            tax_percentage = 0.05

        if product.strip().lower() in self.products_tax["regular_tax"]["products"]:
            tax_percentage += self.products_tax["regular_tax"]["amount"]
        
        return tax_percentage
    
    # calculate the total amount of the receipt
    def total_receipt(self):
        amount = 0
        for product in self.carts:
            amount += self.calculate_price(*product)
        return format(amount,'.2f')
    
    # calculate the total sales tax in a receipt
    def total_sales_tax(self):
        amount = 0
        for product in self.carts:
            amount += self.calculate_sales_tax(*product)
        return format(amount,'.2f')
    
    # rounding up to the nearest 0.05
    def round_decimals_up(self,number, round=0.05):
        round_num = math.ceil(number/round)*round
        return round_num