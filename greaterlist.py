num_list = [1, 6, 32, 93, 71, -20, 30, -90, 50]
# Write your code here
n=int(input())
newlist=[]
for i in range(0,len(num_list)):
    if(num_list[i]>n):
        d=num_list[i]
        newlist=newlist+[d]
print(newlist)
