class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for moreNums in nums:
            self.result += moreNums
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for moreNums in nums:
            self.result -= moreNums
        return self

    def print_result(self):
        print(self.result)
        return self

newEquation = MathDojo()
newEquation.add(5, 0, 8, 5).subtract(2, 2, 4, 6).print_result()