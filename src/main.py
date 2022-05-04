import csv
from shopping import ShoppingCart

def printing_instruction():
    instructions = ["1.Add item to cart","2.Preview receipt","3.Print receipt to csv","4.New Sales"]
    for instruction in instructions:
        print(instruction)

def main():
    printing_instruction()
    sc = ShoppingCart()
    while True:
        user_input = input("Enter options 1,2,3, or 4: ")
        try:
            if int(user_input) == 1:
                try:
                    item = input("Add item to cart in this format => (qty,product,price):")
                    item_data = item.split(",")
                    if len(item_data) != 3:
                        print("Item is not added, please add item using this format => (qty,product,price)")
                        continue
                    sc.add_product(int(item_data[0].strip()),item_data[1],float(item_data[2]))
                except:
                    print("Item is not added, please enter number for qty and price of the product")
            elif int(user_input) == 2:
                sc.preview_receipt()
            elif int(user_input) == 3:
                with open("receipt.csv","w",newline="") as file:
                    writer = csv.writer(file)
                    for item in sc.carts:
                        product_price = sc.calculate_price(*item)
                        writer.writerow([item[0],item[1],format(product_price,'.2f')])
                    file.write("\n")
                    file.write(f"Sales Taxes: {sc.total_sales_tax()}\n")           
                    file.write(f"Total: {sc.total_receipt()}")
                self.carts = []
            elif int(user_input) == 4:
                sc.carts =[]          
        except:
            print("Please select from the options available")
            continue