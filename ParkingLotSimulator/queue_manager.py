from collections import deque

class QueueManager:
    def __init__(self):
        self.queue = deque()

    def add_to_queue(self, vehicle):
        self.queue.append(vehicle)

    def remove_from_queue(self):
        if self.queue:
            return self.queue.popleft()

    def peek_queue(self):
        if self.queue:
            return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0
