n=100
primes=[1]*n
primes[0]=primes[1]=0
def create_seive():
    for i in range(2,n):
        if primes[i]==1:
            for j in range(i*i,n,i):
                primes[j]=0
create_seive()
m=int(input())
n=int(input())
counter=False
for i in range(m,n):
    if(primes[i]==1):
        print(i)
        counter=True
        break
if(counter==False):
    print("No prime numbers in the given range")
