f = open("file.text", "r")
s = f.readlines()
f.close()
f = open("newstates2.txt", "w")

new_list=[]

for line in s:
    # print(line.split())
    reverse_list=[]
    for word in line.split():
        reverse_list.append(word[::-1])
    l2=(" ".join(reverse_list))
    new_list.append(l2)

print(new_list )

