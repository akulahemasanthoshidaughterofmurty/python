mess=input()
for i in mess:
    if(i.isdigit()):
        count=1
        break
    else:
        count=0
if count==1:
    print("Valid Password")
else:
    print("Invalid Password")
