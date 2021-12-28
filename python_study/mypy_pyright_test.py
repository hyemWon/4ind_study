from typing import List, Tuple, Dict

int_var: int = 88
str_var: str = 'hello world'
float_var: float = 88.9
bool_var: bool = True

list_var: List[str] = ["1", "2", "3"]
tuple_var: Tuple[int, ...] = (1, 3, 4)
dic_var: Dict[str, int] = {"key": 3}

def type_check(obj, typer) -> None:
    if isinstance(obj, typer):
        pass
    else:
        raise TypeError(f"Type Error : {typer}")


def cal_add(x: int, y: int) -> int:
    # type_check(x, int)
    # type_check(y, int)
    return x + y

print(cal_add(1, 3))
# print(cal_add(1, 'g'))

# mypy 패키지는 타입체크 자동으로 해줌. 결과값은 볼 수 없다.
# mypy 실행파일.py && python 실행파일.py
