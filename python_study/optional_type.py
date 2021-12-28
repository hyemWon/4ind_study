# Optional type
# 있을 수도 있고 없을 수도 있음
from typing import Union, Optional


def foo(name: str) -> Optional[str]:
    if name == "helena":
        return None
    else:
        return name


# xxx: Union[str, None] = "helena"
# xxx: Optional[str] = 'helena'
# xxx = None

xxx: Optional[str] = foo('helena')
print(xxx)