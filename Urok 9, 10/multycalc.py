from calculator import Calculator


class MultyCalc(Calculator):
    nums = []

    def __init__(self, *args):
        Calculator.__init__(self)
        for argument in args:
            self.nums.append(argument)

    def __str__(self):
        print(f"Список чисел: {self.nums}\n")
        print(f"Сумма чисел: {self.sum()} \n")
        print(f"Разность чисел: {self.min()}\n")
        print(f"Произведение чисел: {self.mult()}\n")
        print(f"Частное чисел: {self.div()}\n")
        return str(self.nums)

    def sum(self):
        sum = 0
        for num in self.nums:
            sum += num
        return sum

    def min(self):
        num1 = self.nums[0]
        for num in self.nums[1:]:
            num1 -= num
        return num1

    def div(self):
        num1 = self.nums[0]
        try:
            for num in self.nums[1:]:
                num1 /= num
        except Exception as err:
            print(type(err))

        except ZeroDivisionError:
            print("! На 0 делить нельзя!")

        else:
            return num1

    def mult(self):
        mult = 1
        for num in self.nums:
            mult *= num
        return mult

