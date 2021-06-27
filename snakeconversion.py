s=input()
for i in range(1,len(s)):
    if(s[i].isupper()):
        index=i
        first=s[1:i]
        second=s[i+1:]

res=s[0].lower()+first+"_"+s[index].lower()+second

print(res)
