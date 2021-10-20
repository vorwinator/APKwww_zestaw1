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
#zad 6
class ScienceCalculator(Calculator):

    def __init__(self):
        self

    def power(self, a, b):
        return a**b

    def invert(self, a):
        if a == 0:
            return("error")
        else:
            return 1/a
print('\n')
print(ScienceCalculator().add(5, 5))
print(ScienceCalculator().power(5, 5))
print(ScienceCalculator().invert(5))
print(ScienceCalculator().invert(0))