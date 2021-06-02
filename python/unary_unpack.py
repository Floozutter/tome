"""
getting the value out of a singleton set!
"""

from typing import TypeVar, NoReturn
T = TypeVar("T")

def unary_unpack(singleton: set[T]) -> T:
    value ,= singleton
    return value

if __name__ == "__main__":
    singleton = {0xdeadbeef}
    empty: set[NoReturn] = set()
    some = {2, 3, 5}
    many = {range(1_000_000)}
    print(unary_unpack(singleton))
