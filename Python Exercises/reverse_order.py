original_list = [1, 2, 3, 4, 5]

reversed_list = []
for value in original_list:
  reversed_list = [value] + reversed_list
print("List after reverse : ", reversed_list)