"""
typing a function with default arguments as a Callable just works!
"""

from typing import Callable

def defaulter(a: int, b: int = 0) -> bool:
    return a + b == 0

unary_callback: Callable[[int], bool] = defaulter
binary_callback: Callable[[int, int], bool] = defaulter

if __name__ == "__main__":
    assert unary_callback(0)
    assert binary_callback(-1, +1)
