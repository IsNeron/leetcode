class CustomStack:

    def __init__(self, maxSize: int):
        self.result = []
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if len(self.result) < self.max_size:
            self.result.append(x)

    def pop(self) -> int:
        if self.result:
            return self.result.pop()
        else:
            return -1 

    def increment(self, k: int, val: int) -> None:
        counter = 0
        
        if k > len(self.result):
            counter = len(self.result)
        elif k < len(self.result):
            counter = k
        else:
            counter = len(self.result)

        for i in range(0, counter):
            self.result[i] += val
            