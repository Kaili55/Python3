class Calculator:
    a = 0
    b = 0

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def __str__(self):
        return \
            f"Num a: {self.a}\n" \
            f"Num b: {self.b}\n" \
            f"a + b: {self.sum()} \n" \
            f"a - b: {self.min()}\n" \
            f"a * b: {self.mult()}\n" \
            f"a / b: {self.div()}\n"

    def sum(self):
        return self.a + self.b

    def min(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def div(self):
        try:
            self.a / self.b
        except Exception as err:
            print(type(err))

        except ZeroDivisionError:
            print("! На 0 делить нельзя!")

        else:
            return self.a / self.b
