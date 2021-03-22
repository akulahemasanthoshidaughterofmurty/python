n=int(input())
new=[]
for i in range(n):
    l=input()
    new+=[l]
reverse=[]
reverse=new[::-1]
for j in range(n):
    print(reverse[j])
