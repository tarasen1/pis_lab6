
class Sample():
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def add(self, a, b):
        return a + b

    def sub(Self, a, b):
        return a - b


if __name__ == '__main__':
    sample = Sample(1,2,3)
    sample.add(1,'a')
