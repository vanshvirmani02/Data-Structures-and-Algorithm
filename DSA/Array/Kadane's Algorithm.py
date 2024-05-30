# Brute Froce
'''arr=[1,2,7,-4,3,2,-10,9,1]
n=len(arr)
sum=0
maxi=float("-inf")
my_dict=dict()
for i in range(n):
    sum = sum + arr[i]
    if sum not in my_dict:
        my_dict[sum]=i

for key,value in my_dict.items():
    maxi=max(key,maxi)
print(maxi)'''

#################################################################################

#Optimal Solution
#Kadane's Algorithm
#TC-O(N)
# SC-O(1)

arr=[10,20,-30,40,-50,60]
def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        sum=0
        maxi=float("-inf")
        i=0
        while i <n:
            sum = sum + nums[i]
            if sum>=0:
                maxi=max(sum,maxi)
            if sum<0:
                maxi=max(sum,maxi)
                sum=0
            i+=1
        return maxi
