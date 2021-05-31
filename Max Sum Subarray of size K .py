n=[1,2,3,4]
k=int(input())
total=0
res=0
for i in range(len(n)):
    total=sum(n[i:i+k])
    res=max(res,total)
print(res)
