#!/usr/bin/env python3
"""Duck typ first element of a seq"""

from typing import Optional, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """function that receives a list"""

    if lst:
        return lst[0]
    else:
        return None
