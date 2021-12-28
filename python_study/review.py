# 제네릭 타입
# 데이터 형식에 의존하지 않고, 하나의 값이 여러 다른 데이터 타입들을 가질 수 있는 기술

from typing import TypeVar, Generic, Optional

T = TypeVar("T", int, float, str)
K = TypeVar("K", int, float, str)

class Robot(Generic[T, K]):
    def __init__(self, arm: T, head: K):
        self.arm = arm
        self.head = head

    def decode(self):
        bbb: Optional[T] = None
        pass

robot1 = Robot[int, int](12314, 2435235)
robot2 = Robot[str, int]("1241345", 66435)
robot3 = Robot[float, str](253245, "425663")

class Siri(Generic[T, K], Robot[T, K]):
    pass

siri1 = Siri[int, int](25235, 666)


def text(x: T) -> T:
    print(x)
    return x