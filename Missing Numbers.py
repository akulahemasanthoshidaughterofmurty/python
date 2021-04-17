n=input()
test_list=n.split()
test_list = [int(i) for i in test_list]
i=0
total=0
result=[]
while(i<=len(test_list)-1):
    total=total+1
    if(total!=test_list[i]):
        result.append(total)
    else:
        i=i+1
print(result)

    
    
