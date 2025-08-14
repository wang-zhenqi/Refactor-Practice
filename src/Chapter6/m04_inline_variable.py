def generate_greeting(name, age, city):
    return f"Hello! Name: {name}, Age: {age}, City: {city}"


print(generate_greeting("Alice", 30, "New York"))

"""def calculate_shipping_cost(weight, distance, rate_per_kg, rate_per_km):
    # 计算重量费用
    weight_cost = weight * rate_per_kg
    # 计算距离费用
    distance_cost = distance * rate_per_km
    # 计算总配送费用
    total_shipping_cost = weight_cost + distance_cost
    return round(total_shipping_cost, 2)


# 调用函数
shipping_cost = calculate_shipping_cost(10, 100, 0.5, 0.2)
print(f"Shipping Cost: {shipping_cost}")
"""
