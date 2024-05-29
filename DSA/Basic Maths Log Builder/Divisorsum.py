#Brute Force Code


def sumOfAllDivisors(n: int) -> int:
    total = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            if i%j==0:
                total += j 
    return total

print(sumOfAllDivisors(5))

#Better solution--> inner loop will run till sqr


#Optimal Solution
sum = 0
n=5
for i in range(1,n+1):
    sum = sum + i*(n//i)

# 1 --> 1
# 2 --> 1 2
# 3 --> 1 3
# 4 --> 1 2 4 
# 5 --> 1 5 
# pattern dekho to hr number n se divide kro to answer baar aa rha hai mtlb ki pehle i 1 hai 5//1 = 5 aur 1 5 baar aa rha hai and same for all 