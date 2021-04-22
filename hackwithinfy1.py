t=int(input())
for tc in range(t):
    n=int(input())
    itemlist=list(map(int,input().split()))
    i=0
    max=0
    itemtype=itemlist[0]
    while i<n:
        c=1
        j=i+1
        while j<n:
            if itemlist[i]==itemlist[j] and j!=i+1:
                c+=1
                #if j<n-1 and itemlist[j]==itemlist[j+1]:
                    #j+=1
            j+=1
        if max<c:
            max=c
            itemtype=itemlist[i]
        i+=1
    print(itemtype)
