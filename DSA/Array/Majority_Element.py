#Brute Force
# TC=O(N*N)
# SC=O(1)
'''arr = [2, 2, 1, 3, 1, 1, 3, 1, 1]
n=len(arr)
element=''
for i in range(n):
    count=arr.count(arr[i])
    if count > n//2:
        element=arr[i]

print(element)'''

#Better Solution /Optimal 
# TC=O(N+N)~O(N)
# SC=O(N)

'''arr = [2, 2, 1, 3, 1, 1, 3, 1, 1]
n=len(arr)
my_dict=dict()
for i in range(n):
    if arr[i] in my_dict:
        my_dict[arr[i]]+=1
    else:
        my_dict[arr[i]]=1

major=n//2
max_element=''
for key,value in my_dict.items():
    if value > major:
        max_element=key
print(max_element)'''


######################################################################

#optimal in case of space

arr = [2, 2, 1, 3, 1, 1, 3, 1, 1]
n=len(arr)
c=arr[0]
count=0

for i in range(0,n):
    if arr[i]==c:
        count+=1
    else:
        count-=1
    if count==0:
        c=arr[i]
        count=1
print(c)
