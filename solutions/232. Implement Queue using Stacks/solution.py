# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


class MyQueue:
    def __init__(self):
        self.inque = []
        self.deque = []

    def push(self, x: int) -> None:
        self.inque.append(x)

    def pop(self) -> int:
        if not self.deque:
            while self.inque:
                cur_elt = self.inque.pop()
                self.deque.append(cur_elt)
        pop_elt = self.deque.pop() if self.deque else None
        return pop_elt

    def peek(self) -> int:
        if not self.deque:
            return self.inque[0] if self.inque else None
        return self.deque[-1] if self.deque else None

    def empty(self) -> bool:
        return not (self.inque or self.deque)
