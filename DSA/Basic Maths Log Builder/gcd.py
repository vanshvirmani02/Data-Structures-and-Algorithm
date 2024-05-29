def gcd(n,m):
    while m!=0:
        n,m=m,n%m
    return n

print(gcd(4,6))
print(gcd(6,9))
print(gcd(2,5))