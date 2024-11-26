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

    #
