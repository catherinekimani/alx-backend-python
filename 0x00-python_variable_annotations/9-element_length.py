#!/usr/bin/env python3
""" Type annotation element length """
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each elem in the input list
    """
    return [(i, len(i)) for i in lst]
