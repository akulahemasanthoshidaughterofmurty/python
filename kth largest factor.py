n=int(input())
l=[]
l.insert(0,0)
for i in range(1,n+1):
    if(n%i==0):
        l.append(i)
index=int(input())
print(l[-index])
