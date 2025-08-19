# 全局变量：当前库存（但名字叫 temp_data？）
temp_data = 150

# 常量：库存警戒线（但命名全小写，且名字无意义）
threshold = 50


def check_stock(order_qty):
    # 局部变量：剩余库存（但叫 data？）
    data = temp_data - order_qty

    # 局部变量：是否需要警告（但叫 flag？）
    flag = False
    if data < threshold:
        flag = True

    # 输出结果（但 result 含义模糊）
    result = "Low Stock Warning" if flag else "Stock OK"
    print(result)

    return flag
