def calculate_total_cost(price, quantity, tax_rate, discount_rate):
    # 计算总成本，包括税和折扣
    net_rate = 1 - discount_rate
    tax_inclusive_rate = 1 + tax_rate
    return round(price * quantity * tax_inclusive_rate * net_rate, 2)


# 调用函数
total_cost = calculate_total_cost(100, 5, 0.15, 0.1)
print(f"Total Cost: {total_cost}")


"""
思考：
对于价格计算的表达式 `(price * quantity * (1 + tax_rate)) * (1 - discount_rate)` 有两种提取方式，
上述的作为方式A，下面的作为方式B。

```python
# Method B
def calculate_total_cost(price, quantity, tax_rate, discount_rate):
    base_price = price * quantity
    price_with_tax = base_price * (1 + tax_rate)
    total = price_with_tax * (1 - discount_rate)
    return round(total, 2)
```

为什么要采用方式A，而不是方式B？

因为从理解代码的难度来看，原始的代码表述和方式B没有什么区别，单看返回值时都只能知道该函数返回的是一个总价，
但总价是如何计算出来的，还是要通读一遍所有的表达式。为了知道总价的计算方法，就需要阅读含税价格的计算方法，
进而需要查看基础价格的定义，还需要理解 `1 + tax_rate` 和 `1 - discount_rate` 的含义。

而方式A中，明确可以知道总价的计算是由四个因子相乘得到的，
每个因子的含义也都清晰（价格、数量、含税率、净价率），只有需要知道含税率和净价率的算法时才需要向上查看定义。
这样一来，简化阅读难度的目的就达到了。

另外，数字和变量的组合对于阅读代码来说也不太好理解，而给它们一个名称，就容易得多了。
"""
