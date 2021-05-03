n=int(input())
for i in range(1,n+1):
    if(i>2) and (i<n):
        hallowspaces="  "*(i-2)
        print("1 "+hallowspaces+""+str(i))
    else:
        stri=""
        for i in range(1,i+1):
            stri=stri+str(i)+" "
        print(stri)
