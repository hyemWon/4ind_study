# 제네릭 타입
# 데이터 형식에 의존하지 않고, 하나의 값이 여러 다른 데이터 타입들을 가질 수 있는 기술
from typing import Union, Optional, TypeVar, Generic

T = TypeVar("T", int, float, str) # ARM이라는 타입변수
K = TypeVar("K", int, float, str)

# 제네릭변수 ARM은 인스턴스에 대한 타입을 지정
class Robot(Generic[T, K]):
    def __init__(self, arm: T, head: K):
        self.arm = arm
        self.head = head

    def decode(self):
        # 암호를 해독하는 코드 (복잡)
        # int일수도 str일수도있는데 복잡한 해독 코드라 경우를 나누기 힘들다.
        bbb: Optional[T] = None
        pass


robot1 = Robot[int, int](122314, 2415235)
robot2 = Robot[str, int]("2415235235", 124134235)
robot3 = Robot[float, str](34123423, "4134235436")

class Siri(Generic[T, K], Robot[T, K]):
    pass

siri1 = Siri[int, int](122314, 2415235)
siri2 = Siri[str, int]("2415235235", 124134235)
siri3 = Siri[float, str](34123423, "4134235436")
print(siri1.arm)

# * function

def test(x: T) -> T:
    print(x)
    print(type(x))
    return x

test(898)