# Brute Force 
# TC=O(N^3)
# SC=O(1)

'''target = 3
arr = [1, 2, 3, 1, 1, 1, 1]
n=len(arr)
max_length=0
for i in range(0,n):
    for j in range(i,n):
        sum=0
        for k in range(i,j+1):
            sum += arr[k]
        if target == sum:
            max_length = max(max_length,j-i+1)
        if target<sum:
            break
print(max_length)'''


#Alternative Brute Force is 
# TC=O(N^2)
# i n times chalega but j sum of n numbers i.e. n(n+1)/2 times
'''target = 3
arr = [1, 2, 3, 1, 1, 1, 1]
n=len(arr)
max_length=0
for i in range(0,n):
    sum=0
    for j in range(i,n):  
        sum += arr[k]
    if target == sum:
        max_length = max(max_length,j-i+1)
    if target<sum:
        break
print(max_length)'''

#######################################################################################################################################################



