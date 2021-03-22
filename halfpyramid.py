n=int(input())
number=1

for i in range(1,n+1):
    pattern=""
    
    for j in range(i):
        pattern=pattern+(str(number)+" ")
        number=number+1
    print(pattern)
        
