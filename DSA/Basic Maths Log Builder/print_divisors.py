#BRUTE-FORCE
# TC= O(N)



# Problem statement
# Given an integer ‘N’, your task is to write a program that returns all the divisors of ‘N’ in ascending order.
# n=int(input())
# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=" ")

#Better Solution 
# TC = O(N/2) ~ O(N)
#range half tk jayegi
# def printDivisors(n: int):
#     List = []
#     num = int(n//2)
#     for i in range(1,num+1):
#         if n%i==0:
#             List.append(i)
#             List.append(n//i)
#     List.sort()
#     return List




# Optimal Solution
# TC = O(N)(for loop) + O(N log N)(for sorting) = O(N + N log N)
# Doubt sort nhi krenge list ko ? Krenge
#This is not optimal solution in this case but sorting is removed it is optimal
# n=int(input())
# num = int(n**0.5)
# for i in range(1,num+1):
#     if n%i==0:
#         print(i,n//i,end=" ")
def printDivisors(n: int):
    List = []
    num = int(n**0.5)
    for i in range(1,num+1):
        if n%i==0:
            List.append(i)
            if n//i != i: #this is used instead of membership operator becuase memberhip has more TC
                List.append(n//i)
    List.sort()
    return List
    # for i in range(1,n+1):
    #     if n%i==0:

print(printDivisors(10))

# import math 
# math.sqrt(num) 
# This is a way to find root using math library