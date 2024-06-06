# Find X in an array using Binary Search
# TC=O(log base2 N)=O(LOgN)
# SC=O(1)

def search(nums: [int], target: int):
    n=len(nums)
    l=0
    h=n-1
    while l<=h:
        mid=(l+h)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            l=mid+1
        else:
            h=mid-1
    return -1


nums = [1, 3, 7, 9, 11, 12, 45]
target = 1
print(search(nums,target))