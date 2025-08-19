from typing import Union

_temp_data: int = 150
REORDER_THRESHOLD = 50


def current_stock() -> int:
    return _temp_data


def check_stock(order_quantity: int) -> dict[str, Union[str, bool]]:
    remaining_stock: int = current_stock() - order_quantity
    is_low_stock: bool = True if remaining_stock < REORDER_THRESHOLD else False

    stock_status_message: str = "Low Stock Warning" if is_low_stock else "Stock OK"
    print(stock_status_message)

    return {
        "stock_status_message": stock_status_message,
        "is_low_stock": is_low_stock,
    }
