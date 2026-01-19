from typing import Dict, Set, List, Tuple
from decimal import Decimal
import threading

products_by_id: Dict[str, dict] = {}
category_index: Dict[str, Set[str]] = {}
price_index: List[Tuple[Decimal, str]] = []

# =========================
# INVENTORY & CONCURRENCY
# =========================

product_locks: Dict[str, threading.Lock] = {}

# =========================
# CART MANAGEMENT
# =========================

carts: Dict[str, dict] = {}

# =========================
# ORDERS
# =========================

orders: Dict[str, dict] = {}
user_orders: Dict[str, List[str]] = {} 
