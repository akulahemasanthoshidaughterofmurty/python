

def findIndex(arr,X,Y,N):
    # Your code goes here
    counterx=countery=0
    i=0
    first=arr.index(X)
    last=arr.index(Y)
    if(last<first):
        start=last
    else:
        start=first
    res=0
    for i in range(start,n):
        if(arr[i]==X):
            counterx+=1
        elif arr[i]==Y:
            countery+=1
        if(counterx==countery):
            res=max(res,i)
            
            
    if(res==0):
        return -1
    elif(res>0):
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    #n=int(input())
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    y=l[2]
    a = list(map(int,input().split()))
    ans=findIndex(a,x,y,n)
    print(ans)

# } Driver Code Ends
