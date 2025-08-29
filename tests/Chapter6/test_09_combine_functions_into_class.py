from Chapter6.m09_combine_functions_into_class import OrderDiscounts


def test_format_order_summary_1():
    assert (
        OrderDiscounts(100, "gold", False).format_order_summary()
        == """订单原价: 100 元
折扣详情: 黄金会员折扣 10%
折后价格: 90.0 元
配送: 需支付运费
"""
    )
