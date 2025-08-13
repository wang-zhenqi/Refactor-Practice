def calculate_total_cost(price, quantity, tax_rate, discount_rate):
    # 计算总成本，包括税和折扣
    total = (price * quantity * (1 + tax_rate)) * (1 - discount_rate)
    return round(total, 2)


# 调用函数
total_cost = calculate_total_cost(100, 5, 0.15, 0.1)
print(f"Total Cost: {total_cost}")
