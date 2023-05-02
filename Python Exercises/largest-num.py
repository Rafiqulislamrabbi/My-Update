# Write a function that takes in a list of numbers and returns the largest number in the list.

def max_num(list1):
    list1.sort()
    return list1[-1]

list1 = [10, 20, 4, 45, 99,101,4,3]
print(max_num(list1))

