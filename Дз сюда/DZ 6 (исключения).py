
# result = []
#
#
# def divider(a, b):
#     if a < b:
#         raise ValueError
#     if b > 100:
#         raise IndexError
#     return a / b
#
#
# data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}
#
#
#
#
# print(result)



result = []


def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b


# data = {10: 2, 2: 5, "123": 4, tuple([]): 15, 18: 0, 8: 4}
data_list = [10, 2, 2, 5, "123", 4, [], 15, 18, 0, 8, 4]
data = {}
i = 1
for key in data_list[::2]:
    try:
        data[key] = data_list[i]
    except Exception as error:
        print(error)
    i += 2


for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as error:
        print(error)


print(result)
