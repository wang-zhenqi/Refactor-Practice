def generate_greeting(name, age, city):
    return f"Hello! Name: {name}, Age: {age}, City: {city}"


print(generate_greeting("Alice", 30, "New York"))

"""
有一些例子并不适用于内联变量这一重构手法，或者说至少没有太大的必要，例如下面的代码。

```
def calculate_shipping_cost(weight, distance, rate_per_kg, rate_per_km):
    weight_cost = weight * rate_per_kg
    distance_cost = distance * rate_per_km
    total_shipping_cost = weight_cost + distance_cost
    return round(total_shipping_cost, 2)

shipping_cost = calculate_shipping_cost(10, 100, 0.5, 0.2)
print(f"Shipping Cost: {shipping_cost}")
```

对上述代码进行重构时，确实可以将 `weight_cost` 和 `distance_cost` 内联进 `total_shipping_cost`
的表达式中，但是原本的变量可以很好地描述计算过程，指明数据的含义，如果只是为了简化代码将它们内联了，反而会丧失一定的可读性。

“内联变量”适用于以下情况：

- 临时变量的赋值表达式非常简单，直接内联不会影响代码的可读性。
- 临时变量只被使用一次，且没有其他逻辑依赖。
- 你希望减少代码中的变量数量，使代码更加简洁。
"""
