# Better Solution
# TC=O(N)
# SC=O(N)
# This is optimal for positive and negative numbers
'''target = 3
arr = [1, 2, 3, 1, 1, 1, 1]
n=len(arr)
max_length = 0 
my_dict=dict()
sum=0
for i in range(n):
    sum = sum + arr[i]

    if sum not in my_dict:
        my_dict[sum]=i
    
    if sum == target:
        max_length=i+1
    
    rem = sum-target
    if rem in my_dict:
        max_length=max(max_length,i-my_dict[rem])

print(max_length)'''

#############################################################

# Optimal Solution only for +ve num 
# Tc= O(2N) ~ O(N)
# SC=O(1)
target = 2
arr = [1,2,1,3]
n=len(arr)
max_length = 0 
r,l=0,0
sum = 0
while r<n:
    while sum>target and l<=r :
        sum = sum - arr[l]
        l+=1
    if sum == target:
        max_length=max(max_length,r-l+1)
    r+=1
    if r<n:
        sum += arr[r]
print(max_length)
