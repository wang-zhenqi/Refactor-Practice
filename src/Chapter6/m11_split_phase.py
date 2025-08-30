from pydantic.dataclasses import dataclass


@dataclass
class Order:
    amount: float
    category: str
    customer_level: str


def calculate_discount(raw_order_data):
    order: Order = parse_order_data(raw_order_data)

    discount_amount: float = calculate_discount_amount(order)

    return round(discount_amount, 2)


def calculate_discount_amount(order: Order) -> float:
    base_discount_of_levels: dict[str, float] = {
        "premium": 0.15,
        "gold": 0.10,
        "silver": 0.05,
    }
    base_discount: float = base_discount_of_levels.get(order.customer_level, 0.0)

    bonus_by_category: dict[str, float] = {
        "electronics": 0.05,
        "clothing": 0.08,
        "books": 0.02,
    }
    category_bonus: float = bonus_by_category.get(order.category, 0.0)

    return order.amount * (base_discount + category_bonus)


def parse_order_data(raw_order_data: str) -> Order:
    parts = raw_order_data.split(",")
    return Order(
        amount=(float(parts[1].strip())),
        category=(parts[2].strip()),
        customer_level=(parts[0].strip()),
    )
