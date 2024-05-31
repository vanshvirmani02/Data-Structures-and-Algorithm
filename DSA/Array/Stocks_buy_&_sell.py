#Brute Force
# TC-O(N**2)
# Sc-O(1)

'''arr=[7 ,1 ,5 ,4 ,3,6]
max_profit=0
n=len(arr)

for i in range(0,n):
    for j in range(i+1,n):
        profit=arr[j]-arr[i]
        max_profit=max(max_profit,profit)

print(max_profit)'''

#############################################################################################################

#Optimal Solution

arr=[5,4,3,2,1]
max_profit=0
n=len(arr)
low=float("inf")

for i in range(n):
    low=min(low,arr[i])
    profit=arr[i]-low
    max_profit=max(max_profit,profit)
print(max_profit)
