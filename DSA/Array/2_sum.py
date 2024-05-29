# Brute Force
# TC=O(N*2)~O(N+sum of n natural numbers) -> n(n+1)/2
# SC=O(1)

'''arr=[5,3,1,6,9,15]
target=12
i=0
n=len(arr)
for i in range(n-1):
    for j in range(i+1,n):
        if arr[i]+arr[j]==target:
            print(i,j) '''



#############################################################

#Optimal Solution
'''arr=[575,330,339,584,239,31,173,929,967]
target=204
n=len(arr)
my_dict=dict()

for i in range(n):
    rem=target-arr[i]
    if rem in my_dict:
        print(i,my_dict[rem])
    my_dict[arr[i]]=i'''



def read(n: int, book: [int], target: int) -> str:
    my_dict=dict()

    for i in range(n):
        rem=target-book[i]
        if rem in my_dict:
            # return [i,my_dict[rem]]
            return "Yes"
        my_dict[book[i]]=i


n=9 
target=204

book=[575,330,339,584,239,31,173,929,967]
print(read(n,book,target)) 