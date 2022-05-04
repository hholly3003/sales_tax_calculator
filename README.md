# Terminal Application - Sales Tax Calculator

## Installation Guide
*System Requirement*: Ensure that Python3 is installed on your machine.

Once the application file is downloaded to your computer, Navigate to directory of the main.py file that should be available under *src* folder.

Open terminal and type in bellow command::
>python3 main.py

***

## Application Purpose and Scope

**The Sales tax Calculator** is a terminal application that has been deployed for computer users. This application aims to produce a receipt file in csv format based on all items that has been inputted by the user.

Functionally, it should take user input and calculate the price inc taxes for each product, calculate the total receipt and total sales tax included in a receipt.

***
## Features
### Straightforward navigation menu
There are 4 options available:<br />
    1.Add item to cart<br />
    2.Preview receipt<br />
    3.Print receipt to csv<br />
    4.New Sales<br />
In order to select the options, simply enter 1,2,3, or 4 then press Enter button

### Add Item to Cart
In order to add items to the carts, enter 1 and it will prompt user to input the product.<br />
It accepts user input in a strict format and followed by Enter button:
```
Example of user input
Add item to cart in this format => (qty,product,price):1,book,12.49
```

### Preview Receipt
This options to have a preview of the receipt before printing out to the receipt to csv file

### Print receipt to csv
Produce a receipt called `receipt.csv`. Once the receipt print out to csv, it will automatically empty the carts and allow user to input products for new receipt

### New Sales
This options is to empty the cart
***
### Improvement
- Add feature to remove item from the cart
- Storing the item that has been added to the cart but have not print out to csv. This will allow it to store a draft receipt
- Multiple receipt being produced at one run time, at the moment only one receipt at a time.