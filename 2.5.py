n = input()
c = ""
for i in n:
    if i == "a" or i == "A":
        continue
    else:
        c += i
print(c)