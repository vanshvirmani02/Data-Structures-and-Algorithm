#parameter Recursion

# def sumofN(n,sum=0):
#     if n==0:
#         return sum
#     return sumofN(n-1,sum+n)

# print(sumofN(5))



# Functional Recursion

def sumofN(n):
    if n==1:
        return 1
    return n+sumofN(n-1)

print(sumofN(5))