from pydantic.dataclasses import dataclass

BASE_DISCOUNTS: dict[str, float] = {
    "premium": 0.15,
    "gold": 0.10,
    "silver": 0.05,
}

CATEGORY_BONUSES: dict[str, float] = {
    "electronics": 0.05,
    "clothing": 0.08,
    "books": 0.02,
}


@dataclass
class Order:
    amount: float
    category: str
    customer_level: str


def calculate_discount(raw_order_data: str) -> float:
    return round(_discount_amount(_parse_data(raw_order_data)), 2)


def _discount_amount(order: Order) -> float:
    base_discount: float = BASE_DISCOUNTS.get(order.customer_level, 0.0)

    category_bonus: float = CATEGORY_BONUSES.get(order.category, 0.0)

    return order.amount * (base_discount + category_bonus)


def _parse_data(raw: str) -> Order:
    p: list[str] = raw.split(",")
    return Order(
        amount=float(p[1].strip()),
        category=p[2].strip(),
        customer_level=p[0].strip(),
    )
