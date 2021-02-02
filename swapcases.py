menu=input()
stri=""
for i in menu:
    uppercase=i.upper()
    if(uppercase==i):
        stri=stri+i.lower()
    else:
        stri=stri+i.upper()
print(stri)
