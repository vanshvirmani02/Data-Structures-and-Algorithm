#Brute Force
# TC=O(N+N/2)~O(N)
# SC=O(N)
'''arr = [1, 2, -4, -5]
positive=[]
negative=[]
n=len(arr)

for i in range(n):
    if arr[i]>=0:
        positive.append(arr[i])
    else:
        negative.append(arr[i])


num=len(positive)
for i in range(num):
    arr[2*i]=positive[i]
    arr[2*i+1]=negative[i]
print(arr)'''

#############################################################################################################


# Optimal SOlution
# TC=O(N)
# SC=O(N)

arr = [1, 2, -4, -5]
n=len(arr)
positive=0
negative=1
result=[0]*n
for i in range(n):
    if arr[i]>0:
        result[positive]=arr[i]
        positive+=2
    else:
        result[negative]=arr[i]
        negative+=2
print(result)


