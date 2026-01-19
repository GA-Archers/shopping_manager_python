# CORE PRODUCT MANAGEMENT
from decimal import Decimal
from typing import Optional


def add_product(
    product_id: str,
    name: str,
    price: Decimal,
    stock: int,
    category: str
) -> bool:
    """
    Add a new product to inventory
    Returns: True if added, False if product_id already exists
    """
    pass


def get_product(product_id: str) -> Optional[dict]:
    """
    Retrieve product details
    Returns: Product dict or None if not found
    """
    pass


def update_stock(product_id: str, quantity: int) -> bool:
    """
    Update product stock (positive or negative)
    Returns: True if updated, False if invalid or insufficient stock
    """
    pass