nums = [1,1,0,1,1,1]
count=0
max_length=0
n=len(nums)
for i in range(n):
    if nums[i]==1:
        count+=1
    else:
        max_length=max(max_length,count)
        count=0
print(max(max_length,count))