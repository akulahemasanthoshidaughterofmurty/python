n=int(input())
for i in range(1,n+1):
    spaces=(n-i)*" "
    if(i>2)and(i<n):
        hallow_spaces="  "*(i-2)
        pattern="* "+hallow_spaces+"* "
        print(spaces+pattern)
    else:
       
        print(spaces+"* "*i)
