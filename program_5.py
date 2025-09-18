# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost.

# Title: Hotdog
    # Author: Dalila Spencer
    # Date: 2025-09-17

order = input('Do you want a hotdog or a chili dog?: ')
if order.lower() == 'hotdog': price = 3.50
elif order.lower() == 'chili dog': price = 4.50
elif order.lower() == 'no' or 'n':
    print('Ok, have a nice day!')
    exit(0)
else:
    print('Sorry, I don\'t understand that')
    exit(1)

toppings = input(f'Would you like cheese on your {order}? ')
if toppings.lower() == 'yes' or 'y': price = price + 0.5

toppings = input(f'Would you like peppers on your {order}? ')
if toppings.lower() == 'yes' or 'y': price = price + 0.75

toppings = input(f'Would you like grilled onions on your {order}? ')
if toppings.lower() == 'yes' or 'y': price = price + 1.0

tax = price * 0.07
total = price + tax

print(f'price: {price:.2f}')
print(f'tax: {tax:.2f}')
print(f'total: {total:.2f}')
