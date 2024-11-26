
'''225. Implement Stack using Queues
Created on 2024-06-26 21:37:53

@author: MilkTea_shih
'''

#%%    Packages
import MyQueue as Queue  #same as MyQueue below

#%%    Variable
class MyQueue:

    def __init__(self) -> None:
        self.stack_1: list[int] = []
        self.stack_2: list[int] = []

    def __len__(self) -> int:
        return len(self.stack_1) + len(self.stack_2)

    def push(self, x: int) -> None:
        self.stack_1.append(x)

    def pop(self) -> int:
        if self.stack_2:
            return self.stack_2.pop()

        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())

        return self.stack_2.pop()

    def peek(self) -> int:
        if self.stack_2:
            return self.stack_2[-1]

        while self.stack_1:
            self.stack_2.append(self.stack_1.pop())

        return self.stack_2[-1]

    def empty(self) -> bool:
        return not self.stack_1 and not self.stack_2

#%%    Functions
class MyStack_oneQueue_reference:

    def __init__(self) -> None:
        self.queue: MyQueue = MyQueue()
        self.length: int = 0

    def push(self, x: int) -> None:
        self.queue.push(x)
        self.length += 1

    def pop(self) -> int:
        for _ in range(self.length - 1):
            self.queue.push(self.queue.pop())

        self.length -= 1
        return self.queue.pop()

    def top(self) -> int:
        for _ in range(self.length - 1):
            self.queue.push(self.queue.pop())

        result: int = self.queue.pop()
        self.queue.push(result)

        return result

    def empty(self) -> bool:
        return not self.queue

class MyStack_twoQueue:

    def __init__(self) -> None:
        self.queue: MyQueue = MyQueue()
        self.temp_queue: MyQueue = MyQueue()

    def push(self, x: int) -> None:
        self.queue.push(x)

    def pop(self) -> int:
        while len(self.queue) > 1:
            self.temp_queue.push(self.queue.pop())

        result: int = self.queue.pop()
        self.queue, self.temp_queue = self.temp_queue, self.queue

        return result

    def top(self) -> int:
        while len(self.queue) > 1:
            self.temp_queue.push(self.queue.pop())

        result: int = self.queue.pop()
        self.temp_queue.push(result)
        self.queue, self.temp_queue = self.temp_queue, self.queue

        return result

    def empty(self) -> bool:
        return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
