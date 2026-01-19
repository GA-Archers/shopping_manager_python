from typing import Dict, Set, List, Tuple
from decimal import Decimal
import threading

# =========================
# PRODUCT CATALOG
# =========================

products_by_id: Dict[str, dict] = {}
category_index: Dict[str, Set[str]] = {}
price_index: List[Tuple[Decimal, str]] = []

# =========================
# INVENTORY & LOCKS
# =========================

product_locks: Dict[str, threading.Lock] = {}
