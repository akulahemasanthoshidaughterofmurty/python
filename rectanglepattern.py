n=int(input())
m=int(input())
number=1
for i in range(n):
    pattern=""
    for j in range(m):
        pattern=pattern+(str(number)+" ")
        number=number+1
    print(pattern)
