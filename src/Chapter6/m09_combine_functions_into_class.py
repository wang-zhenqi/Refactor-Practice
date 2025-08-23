# order_discounts.py


def calculate_discount(order_amount, customer_level, is_first_order):
    """根据客户等级和是否首单计算折扣率"""
    base_discount = 0.0
    if customer_level == "premium":
        base_discount = 0.15
    elif customer_level == "gold":
        base_discount = 0.10
    elif customer_level == "silver":
        base_discount = 0.05

    first_order_bonus = 0.05 if is_first_order else 0.0
    total_discount = base_discount + first_order_bonus
    return min(total_discount, 0.20)  # 最高不超过20%


def apply_discount(order_amount, customer_level, is_first_order):
    """应用折扣到订单金额"""
    discount_rate = calculate_discount(order_amount, customer_level, is_first_order)
    discounted_amount = order_amount * (1 - discount_rate)
    return round(discounted_amount, 2)


def discount_description(customer_level, is_first_order):
    """生成折扣说明文本"""
    parts = []
    if customer_level == "premium":
        parts.append("尊贵会员折扣 15%")
    elif customer_level == "gold":
        parts.append("黄金会员折扣 10%")
    elif customer_level == "silver":
        parts.append("白银会员折扣 5%")

    if is_first_order:
        parts.append("首单优惠 5%")

    return " + ".join(parts) if parts else "无折扣"


def is_eligible_for_free_shipping(discounted_amount):
    """判断折扣后是否满足包邮条件"""
    return discounted_amount >= 99.0


def format_order_summary(order_amount, customer_level, is_first_order):
    """格式化订单摘要"""
    final_amount = apply_discount(order_amount, customer_level, is_first_order)
    description = discount_description(customer_level, is_first_order)
    shipping_status = "包邮" if is_eligible_for_free_shipping(final_amount) else "需支付运费"

    return f"""订单原价: {order_amount} 元
折扣详情: {description}
折后价格: {final_amount} 元
配送: {shipping_status}
"""


class OrderDiscounts:
    def __init__(self, order_amount: int, customer_level: str, is_first_order: bool):
        self.order_amount = order_amount
        self.customer_level = customer_level
        self.is_first_order = is_first_order

    def _apply_discount(self):
        """应用折扣到订单金额"""
        discount_rate = calculate_discount(self.order_amount, self.customer_level, self.is_first_order)
        discounted_amount = self.order_amount * (1 - discount_rate)
        return round(discounted_amount, 2)

    def format_order_summary(self) -> str:
        """格式化订单摘要"""
        final_amount = self._apply_discount()
        description = discount_description(self.customer_level, self.is_first_order)
        shipping_status = "包邮" if is_eligible_for_free_shipping(final_amount) else "需支付运费"

        return f"""订单原价: {self.order_amount} 元
折扣详情: {description}
折后价格: {final_amount} 元
配送: {shipping_status}
"""
