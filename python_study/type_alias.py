# * Type alias
# 타입 별칭
# 재사용성과 코드 간결화를 위해

from typing import Union, List, Tuple, Dict, Optional
from typing_extensions import TypedDict


value: Union[int, bool, Union[List[str], List[int], Tuple[int, ...]], Optional[Dict[str, float]]] = 17

## 너무 복잡한 타이핑
# def cal(v: Union[int, bool, Union[List[str], List[int], Tuple[int, ...]], Optional[Dict[str, float]]]) -> \
#         Union[int, bool, Union[List[str], List[int], Tuple[int, ...]], Optional[Dict[str, float]]]:
#     # data 처리
#     return v

# 타입에 별칭을 붙여 변수처럼 사용
Value = Union[int, bool, Union[List[str], List[int], Tuple[int, ...]], Optional[Dict[str, float]]]

value: Value = 17

# * Dict alias

ddd: Dict[str, Union[str, int]] = {"hello": "world", "world": "wow!!", "hee": 17}
# Union 쓰면 해결은 된다. 하지만 파이썬에서는 Json 형식이 Dict타입이다.
# 이때에는 key가 정확히 매핑되는데 키값에 따라 타입을 달리 설정해 줄 수 있다.

class Point(TypedDict):
    x: int
    y: float
    z: str
    hello: int

point: Point = {"x": 8, "y": 8.4, "z": "helena", "hello": 12}



