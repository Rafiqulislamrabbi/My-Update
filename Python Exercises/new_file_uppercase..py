f = open("file.text", "rb")
s = f.readlines()
f.close()
f = open("newstates3.txt", "wb")

for line in s:
    f.write(line.upper())
f.close()
