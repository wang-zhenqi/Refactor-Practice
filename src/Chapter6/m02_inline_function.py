def print_invoice(quantity, price):
    total = quantity * price
    print(f"Quantity: {quantity}")
    print(f"Price per item: {price}")
    print(f"Total: {total}")
    return total


# 调用函数
print_invoice(5, 10)


def print_order_summary(item_name, price, quantity, discount_rate):
    total_price = price * quantity
    final_price = round(total_price * (1 - discount_rate), 2)
    print(f"Item: {item_name}")
    print(f"Quantity: {quantity}")
    print(f"Total Price (before discount): {total_price}")
    print(f"Final Price (after discount): {final_price}")
    return final_price


# 调用函数
print_order_summary("Laptop", 1200.50, 2, 0.1)
