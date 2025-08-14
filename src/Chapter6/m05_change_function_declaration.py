def calculate_total_price(items):
    """
    第一阶修改：更改函数名
    """

    total = sum(item["price"] * item["quantity"] for item in items)
    return total


def apply_discount(total_price, discount_rate):
    """
    第二阶修改：增减函数参数
    目标：给函数新增一个 `tax_rate` 参数
    """
    return total_price * (1 - discount_rate)
