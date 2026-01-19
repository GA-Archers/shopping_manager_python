from decimal import Decimal
from common.datastore import (
    products_by_id,
    category_index,
    price_index,
    product_locks
)
import threading
import bisect


def load_demo_products() -> None:
    demo_products = [
        ("p1", "iPhone 14", Decimal("69999"), 10, "electronics"),
        ("p2", "Samsung Galaxy", Decimal("59999"), 15, "electronics"),
        ("p3", "MacBook Air", Decimal("99999"), 5, "electronics"),
        ("p4", "Nike Shoes", Decimal("7999"), 20, "fashion"),
        ("p5", "Office Chair", Decimal("8999"), 12, "furniture"),
    ]

    for product_id, name, price, stock, category in demo_products:
        products_by_id[product_id] = {
            "id": product_id,
            "name": name,
            "price": price,
            "stock": stock,
            "category": category,
            "reservations": {}
        }

        # category index
        category_index.setdefault(category, set()).add(product_id)

        # price index (sorted insertion)
        bisect.insort(price_index, (price, product_id))

        # lock per product
        product_locks[product_id] = threading.Lock()
