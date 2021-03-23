n=input()
number=int(input())
str1=n.split(",")
for i in range(len(str1)):
    str1[i]=int(str1[i])
#str1=sorted(str1,reverse=True)
str1=sorted(str1)
print(str1[number-1])
