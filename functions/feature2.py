# SHOPPING CART OPERATIONS
def add_to_cart(user_id: str, product_id: str, quantity: int) -> bool:
    """
    Add item to user's cart (creates cart if doesn't exist)
    Returns: True if added, False if insufficient stock
    """
    pass


def remove_from_cart(user_id: str, product_id: str) -> bool:
    """
    Remove item from cart
    Returns: True if removed, False if item not in cart
    """
    pass


def get_cart(user_id: str) -> Dict[str, int]:
    """
    Get all items in user's cart
    Returns: Dict {product_id: quantity}
    """
    pass


