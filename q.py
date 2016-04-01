from math import sqrt

def isprime(ans,n):
    up = sqrt(n)
    for p in ans:
        if p > up:
            return True
        if n%p == 0:
            return False
    return True
def getnextprime(ans,n):
    while(not isprime(ans,n)):
        n +=1
    return (ans+[n],n)

def t(n):
    plst = []
    a = 1
    while(n!=1):
        plst, a = getnextprime(plst,a+1)
        while n%a==0:
            n /= a
    print(a)