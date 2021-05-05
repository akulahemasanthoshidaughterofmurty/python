n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
sum=l[0]
print(round(sum/1,3))
j=1
for i in range(1,n):
    j=j+1
    sum=sum+l[i]
    avg=sum/j
    print(round(avg,3))
