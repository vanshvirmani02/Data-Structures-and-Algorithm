# Next Permutation
# Optimal Solution
# TC=O(N+N+N)=O(3N)~O(N)
# SC=O(1)
nums=[2,3,1]
index=-1
n=len(nums)
for i in range(n-2,-1,-1):
    if nums[i]<nums[i+1]:
        index=i
        break
for i in range(n-1,index,-1):
    if nums[i]>nums[index]:
        nums[i],nums[index]=nums[index],nums[i]
=nums[0:index+1]+nums[n-1:index:-1])
if index==-1:
    print(nums.reverse())


def make_reverse(nums,start,end):
    nums[:]=nums[end:start-1:-1]