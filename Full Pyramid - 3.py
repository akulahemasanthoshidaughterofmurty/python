n=int(input())
z=1
t=n
for i in range(n):
   zeros="0 "*(t-1)
   ones="1 "*z
   print(zeros+ones+zeros)
   z+=2
   t=t-1
