n=int(input())
for i in range(1,n+1):
    if(i>2) and (i<n):
        hallow_spaces="  "*(i-2);
        print("* "+hallow_spaces+"* ")
    else:
        print("* "*i)
