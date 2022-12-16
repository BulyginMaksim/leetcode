from collections import deque
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


class MyStack:

    def __init__(self):
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x: int) -> None:
        self.queue_out.append(x)
        while self.queue_in:
            self.queue_out.append(self.queue_in.popleft())
        self.queue_in, self.queue_out = self.queue_out, self.queue_in

    def pop(self) -> int:
        return self.queue_in.popleft() if self.queue_in else None

    def top(self) -> int:
        return self.queue_in[0] if self.queue_in else None

    def empty(self) -> bool:
        return not self.queue_in
