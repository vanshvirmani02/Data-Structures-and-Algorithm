# Brute Force
'''def element(a):
    a[:] = sorted(a)
    return [a[1],a[-2]]

a = [6,2,3,4,66,0,1]
print(element(a))'''


# Better Solution
# Tc=O(2N)~N
# SC=O(1)

'''a = [6,2,3,4,66,0,1]

largest=float("-inf")
smallest=float("inf")
second_largest=float("-inf")
second_smallest=float("inf")

n=len(a)
for i in range(n):
    largest=max(largest,a[i])
    smallest=min(smallest,a[i])

for i in range(n):
    if a[i]<second_smallest and a[i]!=smallest:
        second_smallest=a[i]
    if a[i]>second_largest and a[i]!=largest:
        second_largest=a[i]

print([second_largest,second_smallest])
'''

#Optimal SOlution

arr = [6,2,3,4,66,0,1]

largest=float("-inf")
smallest=float("inf")
second_largest=float("-inf")
second_smallest=float("inf")

n=len(arr)
for i in range(n):
    if arr[i]>largest:
        second_largest=largest
        largest=arr[i]
    if arr[i]<smallest:
        second_smallest=smallest
        smallest=arr[i]
    if arr[i]<largest and arr[i]>second_largest:
        second_largest=arr[i]
    if arr[i]>smallest and arr[i]<second_smallest:
        second_smallest=arr[i]
print(second_largest,second_smallest) 
    
