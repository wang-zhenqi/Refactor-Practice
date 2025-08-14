def generate_greeting(name, age, city):
    # 临时变量：格式化后的姓名和年龄
    formatted_name = f"Name: {name}"
    formatted_age = f"Age: {age}"
    # 临时变量：格式化后的城市
    formatted_city = f"City: {city}"
    # 组合成完整的问候语
    greeting = f"Hello! {formatted_name}, {formatted_age}, {formatted_city}"
    return greeting


# 调用函数
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
