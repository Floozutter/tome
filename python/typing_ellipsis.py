"""
typing Ellipsis as a value!
"""

from typing import Literal

def only_eats_ellipsis(food: "ellipsis") -> Literal["nom nom nom"]:
    assert food is ...
    return "nom nom nom"

if __name__ == "__main__":
    print(f"{only_eats_ellipsis(...)=}")
    print(f"{only_eats_ellipsis(Ellipsis)=}")
    print(f"{only_eats_ellipsis(type(...)())=}")
    print(f"{only_eats_ellipsis(type(Ellipsis)())=}")
    try:
        evil = "only_eats_ellipsis(None)"
        print(f"{evil}=", end = "")
        print(eval(evil))
    except AssertionError:
        print("!")
        print(f"please feed {only_eats_ellipsis} properly!")
