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