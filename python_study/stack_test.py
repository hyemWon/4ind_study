from typing import Optional

class Node:
    def __init__(self, item, pointer: Optional["Node"]=None):
        self.item = item
        self.pointer = pointer


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    @property
    def length(self) -> int:
        if self.head is None:
            return 0
        else:
            count: int = 1
            cur_node: Node = self.head
            while cur_node.pointer is not None:
                cur_node = cur_node.pointer
                count += 1
                print(count)
            print(count)
            return count

class Stack(LinkedList):
    def push(self, item) -> None:
        new_node = Node(item=item)
        if self.head is None:
            self.head = new_node
            return

        cur_node = self.head
        print(cur_node.pointer)
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
            # print(cur_node.item)
        cur_node.pointer = new_node

    def pop(self):
        pass


if __name__=='__main__':
    stack = Stack()
    stack.push(12)
    stack.push(15)
    stack.push(7)
    print(stack.head.item)
    print(stack.length)