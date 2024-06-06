# Generate Permutation Method 2 
# TC=O(N * N!)
# SC=O(N!)
ans=[]

def permutation(nums,index):
    if index==len(nums):
        ans.append(nums.copy())
        return
    for i in range(index,len(nums)):
        nums[index],nums[i]=nums[i],nums[index]
        permutation(nums,index+1)
        nums[index],nums[i]=nums[i],nums[index]
    return ans

nums=[1,2,3]
index=0
print(permutation(nums,index))