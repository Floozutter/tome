"""
the journey of typing an unfillable list!
"""

from typing import Any, NoReturn

"""
attempt 1: list[Any]
- all is subtype of Any, Any is subtype of all ("switch" type (uwu))
- can hold anything and allows anything!
- completely permissive; not what we want...
"""
a: list[Any] = []
a.append(object())
a.append(0xdeadfeed)
a.append("uwu")
tuple(map(str, a))
a[1].bit_length()
a[2].replace("u", "o")

"""
attempt 2: list[object]
- all is subtype of object, but not the other way around (top type)
- can hold anything but only allows what can be done to anything!
- strict in the wrong way; opposite of what we want...
"""
b: list[object] = []
b.append(object())
b.append(0xdeadfeed)
b.append("uwu")
tuple(map(str, b))
#b[1].bit_length()  # type error!
#b[2].replace("u", "o")  # type error!

"""
attempt 3: list[NoReturn]
- NoReturn is subtype of all, but not the other way around (bottom type)
- can't hold anything but allows anything!
- string in the right way; exactly what we want! >:3c
"""
c: list[NoReturn] = []
#c.append(object())  # type error!
#c.append(0xdeadfeed)  # type error!
#c.append("uwu")  # type error!
try:
    hmmm: int = c[0]  # not a type error, but a runtime error!
    uhhh: str = c[0]  # not a type error, but a runtime error!
except IndexError:
    pass
