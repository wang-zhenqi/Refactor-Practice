def print_invoice(quantity, price):
    total = quantity * price
    print(f"Quantity: {quantity}")
    print(f"Price per item: {price}")
    print(f"Total: {total}")
    return total


# 调用函数
print_invoice(5, 10)
