# def bigger(x, y):
#     if x == y:
#         return "Equal"
#     else:
#         if x > y:
#             return x
#         else:
#             return y
#
#
# print(bigger(10, 10))

bigger = lambda x, y: "Equal" if x == y else x if x > y else y
print(bigger(10, 16))
