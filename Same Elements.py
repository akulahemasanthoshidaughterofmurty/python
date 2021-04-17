n=input()
new_list=n.split()
#new_list=list(map(int,input().strip().split()))[:n]
new_set=set()
count=0
item=int(new_list[0])
new_set.add(item)
for i in new_list:
    if(int(i)==item):
        count+=1
    else:
        new_set.add(int(i))
if(count==len(new_list)):
    print("True")
else:
    converted_list=list(new_set)
    sorted_list=sorted(converted_list)
    print(sorted_list)
