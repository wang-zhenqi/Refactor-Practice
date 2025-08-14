def calc_total_price(items):
    """
    第一阶修改：更改函数名
    """

    total = sum(item["price"] * item["quantity"] for item in items)
    return total
