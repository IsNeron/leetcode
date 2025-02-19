class ProductOfNumbers:

    def __init__(self):
        self.collection = []
        

    def add(self, num: int) -> None:
        self.collection.append(num)
        

    def getProduct(self, k: int) -> int:
        res = 1
        for element in self.collection[-k:]:
            res *= element
        return res


# Your ProductOfNumbers object will be instantiated and called as such:
obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
print(obj.getProduct(2)) #20
print(obj.getProduct(3)) #40
print(obj.getProduct(4)) #0
obj.add(8)
print(obj.getProduct(2)) #32
