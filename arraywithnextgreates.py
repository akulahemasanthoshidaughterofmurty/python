l1=[1,2,4]
l2=[1,3,4,2]
n=[]
for i in range(len(l1)):
    ele=l1[i]
    index=l2.index(ele)
    for j in range(index+1,len(l2)):
        if(l2[j]>ele):
            n.append(l2[j])
            break
    else:
            n.append(-1)
print(n)
