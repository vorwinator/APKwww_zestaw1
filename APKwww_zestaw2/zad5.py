class Calculator:
    def __init__(self):
        self

    def add(self, a, b):
        return a+b

    def difference(self, a, b):
        return a-b

    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        if b == 0:
            return("error")
        else:
            return a/b

print(Calculator().add(5, 5))
print(Calculator().difference(5, 5))
print(Calculator().multiply(5, 5))
print(Calculator().divide(5, 5))
print(Calculator().divide(5, 0))