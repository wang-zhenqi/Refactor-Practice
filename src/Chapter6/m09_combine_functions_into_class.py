# order_discounts.py


class OrderDiscounts:
    DISCOUNT_RATE = {
        "premium": 0.15,
        "gold": 0.10,
        "silver": 0.05,
    }

    DISCOUNT_DESCRIPTION = {
        "premium": "尊贵会员折扣 15%",
        "gold": "黄金会员折扣 10%",
        "silver": "白银会员折扣 5%",
    }

    def __init__(self, order_amount: int, customer_level: str, is_first_order: bool):
        self.order_amount = order_amount
        self.customer_level = customer_level
        self.is_first_order = is_first_order

    def _calculate_discount(self) -> float:
        """根据客户等级和是否首单计算折扣率"""
        base_discount = self.DISCOUNT_RATE.get(self.customer_level, 0.0)

        first_order_bonus = 0.05 if self.is_first_order else 0.0
        total_discount = base_discount + first_order_bonus
        return min(total_discount, 0.20)  # 最高不超过20%

    def _apply_discount(self) -> float:
        """应用折扣到订单金额"""
        discount_rate = self._calculate_discount()
        discounted_amount = self.order_amount * (1 - discount_rate)
        return round(discounted_amount, 2)

    def _discount_description(self) -> str:
        """生成折扣说明文本"""
        parts: list[str] = []
        if self.customer_level in self.DISCOUNT_DESCRIPTION:
            parts.append(self.DISCOUNT_DESCRIPTION[self.customer_level])

        if self.is_first_order:
            parts.append("首单优惠 5%")

        return " + ".join(parts) if parts else "无折扣"

    @staticmethod
    def _is_eligible_for_free_shipping(discounted_amount: float) -> bool:
        """判断折扣后是否满足包邮条件"""
        return discounted_amount >= 99.0

    def format_order_summary(self) -> str:
        """格式化订单摘要"""
        final_amount = self._apply_discount()
        description = self._discount_description()
        shipping_status = "包邮" if self._is_eligible_for_free_shipping(final_amount) else "需支付运费"

        return f"""订单原价: {self.order_amount} 元
折扣详情: {description}
折后价格: {final_amount} 元
配送: {shipping_status}
"""
