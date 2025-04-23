prices = {
    'apple': 2.5,
    'banana': 1.0,
    'orange': 1.5,
    'milk': 3.0,
    'bread': 2.0
}
quantities = {
    'apple': 3,
    'banana': 5,
    'orange': 2,
    'milk': 1,
    'bread': 4
}
def calculate(price, quantity):
    total_bill = 0
    for item, price in price.items():
        if item in quantity:
            total_bill += price * quantity[item]
    return total_bill

total_bill = calculate(prices, quantities)
print(f"Total bill: {total_bill:.2f}")  
