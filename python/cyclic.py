"""
cyclic structures in Python!
"""

from typing import Callable

CyclicCallable = Callable[[], "CyclicCallable"]

def cyclic_function() -> CyclicCallable:
    return cyclic_function
assert cyclic_function is cyclic_function()()()

cyclic_lambda: CyclicCallable = lambda: cyclic_lambda
assert cyclic_lambda is cyclic_lambda()()()

CyclicList = list["CyclicList"]
cyclic_list: CyclicList = []
cyclic_list.append(cyclic_list)
assert cyclic_list is cyclic_list[0][0][0]
