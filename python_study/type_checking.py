from typing import List, Tuple, Dict

def type_check(obj, typer) -> None:
    if isinstance(obj, typer):
        pass
    else:
        raise TypeError(f"Type Error : {typer}")


def cal_add(x: int, y: int) -> int:
    type_check(x, int)
    type_check(y, int)
    return x + y

print(cal_add(1, 3))


