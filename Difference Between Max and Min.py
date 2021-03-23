n=input()
str1=n.split(",")
for i in range(len(str1)):
    str1[i]=int(str1[i])
str1=sorted(str1)
small=min(str1)
big=max(str1)
print((big)-(small))
