f = open("file.text", "rb")
s = f.readlines()
f.close()
f = open("newstates2.txt", "wb")
s.reverse()
for line in s:
    f.write(line)
f.close()
