n=input()
list1=[]
for i in n:
    if(i.isdigit()):
        list1+=[i]
for i in range(len(list1)):
    list1[i]=int(list1[i])

print(sum(list1))
print(min(list1))
print(max(list1))
