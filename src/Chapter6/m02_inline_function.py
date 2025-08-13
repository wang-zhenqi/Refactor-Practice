def calculate_total_price(quantity, price):
    return quantity * price


def print_invoice(quantity, price):
    total = calculate_total_price(quantity, price)
    print(f"Quantity: {quantity}")
    print(f"Price per item: {price}")
    print(f"Total: {total}")
    return total


# 调用函数
print_invoice(5, 10)
