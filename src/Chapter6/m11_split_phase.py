from pydantic import BaseModel


class Order(BaseModel):
    amount: float
    category: str
    customer_level: str


def calculate_discount(raw_order_data):
    order: Order = parse_order_data(raw_order_data)

    discount_amount = calculate_discount_amount(order)

    return round(discount_amount, 2)


def calculate_discount_amount(order: Order):
    base_discount_of_levels = {
        "premium": 0.15,
        "gold": 0.10,
        "silver": 0.05,
    }
    base_discount = base_discount_of_levels.get(order.customer_level, 0.0)

    bonus_by_category = {
        "electronics": 0.05,
        "clothing": 0.08,
        "books": 0.02,
    }
    category_bonus = bonus_by_category.get(order.category, 0.0)

    total_discount_rate = base_discount + category_bonus
    discount_amount = order.amount * total_discount_rate
    return discount_amount


def parse_order_data(raw_order_data: str) -> Order:
    parts = raw_order_data.split(",")
    customer_level = parts[0].strip()
    amount = float(parts[1].strip())
    category = parts[2].strip()
    return Order(amount=amount, category=category, customer_level=customer_level)
