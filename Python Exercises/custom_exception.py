def Average(l):
    try:
        avg = sum(l) / len(l)
        return avg
    except ZeroDivisionError:
        return "empty list"
    except Exception:
        return "error"


my_list = [2, 4, 6, 8, "10"]
average = Average(my_list)

print(average)




# def Average(l):
#     try:
#         avg = sum(l) / len(l)
#         return avg
#     except :
#         return "empty list"
#
#
# my_list = []
# average = Average(my_list)
#
# print(average)