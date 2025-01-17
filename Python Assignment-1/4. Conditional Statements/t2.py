# prime number

n =int(input("enter numer : "))

prime=0
for i in range(1,n+1):
    if n%i==0:
        prime +=1

if prime==2:
    print(n,"is prime")
else:
    print(n,"is not prime")
