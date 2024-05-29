#Brute Force
# TC=O(N**2)
# SC=O(1)

'''arr=[0,1,3]
for i in range(len(arr)+1):
    if i not in arr:
        print(i)'''


#Optimal
# TC=O(N)
# SC=O(1)

arr=[0,1,3]
n=len(arr)
total=sum(arr)
missing=(n*(n+1)//2)-total
print(missing)