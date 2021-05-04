n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
print(l[0])
sum=l[0]
for i in range(1,n):
    sum=sum+l[i]
    print(sum)
    
