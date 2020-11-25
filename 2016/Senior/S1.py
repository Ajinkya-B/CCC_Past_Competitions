str1 = str(input())
str2 = str(input())
msg = "A"

str2 = str2.replace("*", "")

for char in str2:
    a = str1.find(char)
    if a != -1:
        str1 = str1[:a] + str1[a+1:]
    else:
        msg = "N"
        break

print(msg)
