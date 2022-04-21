#!/usr/bin/env python3
""" list input of of ints and floats, returns float """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Sum list of of integers and floats """
    return sum(mxd_lst)
