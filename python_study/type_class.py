
# class Hello:
#     def world(self) -> int:
#         return 7
#
# class World:
#     pass
#
# hello: Hello = Hello()
# world: World = World()
#
# def foo(ins: Hello) -> int:
#     return ins.world()
#
# print(foo(hello))
# print(foo(world))


# * class type 보충
# class 에서 자기자신의 타입을 가르킬때 ""따옴표로 감싸야 한다.
from typing import Optional

class Node:
    def __init__(self, data: int, node: Optional["Node"] = None):
        self.data = data
        self.node = node

node2 = Node(12)
node1 = Node(27, node2)
node0 = Node(30, node1)