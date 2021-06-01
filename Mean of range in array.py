    def findMean(self, arr, queries, n, q): 
        # Complete the function
        prefix=[0]*n
        prefix[0]=arr[0]
        for i in range(1,n):
            prefix[i]=prefix[i-1]+arr[i]
        l=0
        list1=[]
        while(l<len(queries)):
            left=queries[l]
            right=queries[l+1]
          
            if(left==0):
                sum=prefix[right]
                length=right-left+1
                list1.append(math.floor(sum//length))
                
            else:
                sum=prefix[right]-prefix[left-1]
                length=right-left+1
                list1.append(math.floor(sum//length))
            l=l+2
        return list1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

    
for _ in range(0,int(input())):
    n,q = map(int,input().strip().split())
    arr = list(map(int,input().strip().split()))
    queries = list(map(int,input().strip().split()))
    ob=Solution()
    v = ob.findMean(arr, queries, n, 2*q)
    print(*v)
    
# } Driver Code Ends
