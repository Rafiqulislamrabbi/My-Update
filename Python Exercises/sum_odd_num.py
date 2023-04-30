# Write a function that takes in a list of numbers and returns the sum of all odd numbers in the list.
def oddsum(list1):
    sum=0
    for i in list1:
        if i%2!=0:
            sum=sum+i
    return sum

print(oddsum([1,2,3,4,5,6,7,8,9]))
