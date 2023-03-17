def int_input(message=''):
    while True:
        try:
            result = int(input(message))

        except ValueError as error:
            print(f"Что-то пошло не так: {error}")

        except Exception as error:
            print(type(error), error)

        else:
            print("Ок, ваше первое число:")
            return result


a = int_input("Введите первое число: ")

print(a)
