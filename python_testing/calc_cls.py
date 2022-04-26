
class Calc:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


    def divide(self):
        if self.b != 0:
            return self.a / self.b
        raise ZeroDivisionError


# c = Calc(4,2)
# c.add() ~ 6
# c.divide ~ 2
