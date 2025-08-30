def calculate_discount(raw_order_data):
    amount, category, customer_level = parse_order_data(raw_order_data)

    discount_amount = calculate_discount_amount(amount, category, customer_level)

    return round(discount_amount, 2)


def calculate_discount_amount(amount, category, customer_level):
    base_discount = 0.0
    if customer_level == "premium":
        base_discount = 0.15
    elif customer_level == "gold":
        base_discount = 0.10
    elif customer_level == "silver":
        base_discount = 0.05
    category_bonus = 0.0
    if category == "electronics":
        category_bonus = 0.05
    elif category == "clothing":
        category_bonus = 0.08
    elif category == "books":
        category_bonus = 0.02
    total_discount_rate = base_discount + category_bonus
    discount_amount = amount * total_discount_rate
    return discount_amount


def parse_order_data(raw_order_data: str) -> tuple[float, str, str]:
    parts = raw_order_data.split(",")
    customer_level = parts[0].strip()
    amount = float(parts[1].strip())
    category = parts[2].strip()
    return amount, category, customer_level
