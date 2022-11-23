from collections import deque


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
class RecentCounter:
    def __init__(self):
        self.queue = deque()
        self.counter = 0

    def ping(self, t: int) -> int:
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
            self.counter -= 1
        self.queue.append(t)
        self.counter += 1
        return self.counter
