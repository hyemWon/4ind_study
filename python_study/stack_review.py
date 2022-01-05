from typing import Optional, Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, item: T, pointer: Optional["Node"]=None):
        self.item = item
        self.pointer = pointer

class LinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None

    @property
    def length(self) -> int:
        if self.head is None:
            return 0
        count: int = 1
        cur_node = self.head
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
            count += 1
        return count


class Stack(Generic[T], LinkedList[T]):
    def push(self, item):
        new_node: Node[T] = Node[T](item=item)

        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
        cur_node.pointer = new_node


    def pop(self):
        if self.head is None:
            raise ValueError("stack is empty!")
        else:
           cur_node = self.head
        
        if cur_node.pointer is None:
            self.head = None
            return cur_node.item

        while cur_node.pointer.pointer is not None:
            cur_node = cur_node.pointer
        
        result = cur_node.pointer.item
        cur_node.pointer = None
        return result


           
      
if __name__=='__main__':
    stack = Stack()
    stack.push(15)
    stack.push(10)
    stack.push(5)
    print(stack.pop())

    stack.push(100)

    print(stack.length)