n=int(input())
squa=n**2
number=1
for i in range(n):
    pattern=""
    for j in range(n):
        pattern=pattern+(str(number)+" ")
        number=number+1
    print(pattern)
