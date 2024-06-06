#Generate Permutations Method 1 
# TC=O(N * N!)
# SC=O(N!)

nums=[1,2,3]
result=[]
ds=[]
freq=[0,0,0]
n=len(nums)
def permutation(nums,freq):
    if len(ds)==len(nums):
        result.append(ds.copy())
        return 
    for i in range(0,n):
        if freq[i]==0:
            ds.append(nums[i])
            freq[i]=1
            permutation(nums,freq)
            freq[i]=0
            ds.pop()
    return result

print(permutation(nums,freq))    