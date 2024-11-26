
'''232. Implement Queue using Stacks
Created on 2024-06-26 20:46:42

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class MyQueue_reference:

    def __init__(self) -> None:
        self.stack: list[int] = []
        self.temp_stack: list[int] = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.temp_stack:
            return self.temp_stack.pop()

        while self.stack:
            self.temp_stack.append(self.stack.pop())

        return self.temp_stack.pop()

    def peek(self) -> int:
        if self.temp_stack:
            return self.temp_stack[-1]

        while self.stack:
            self.temp_stack.append(self.stack.pop())

        return self.temp_stack[-1]

    def empty(self) -> bool:
        return not self.stack and not self.temp_stack

class MyQueue:
    '''
    The element in queue is never released, but time complexity is O(1)
    '''

    def __init__(self) -> None:
        self.queue: list[int] = []
        self.back_index: int = 0
        self.top_index: int = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.back_index += 1

    def pop(self) -> int:
        result: int = self.peek()
        self.top_index += 1

        return result

    def peek(self) -> int:
        return self.queue[self.top_index]

    def empty(self) -> bool:
        return self.back_index == self.top_index


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
