#!/usr/bin/env python3
""" take a float, return a function """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Takes a float and returns a function """
    return (lambda x: multiplier*x)
