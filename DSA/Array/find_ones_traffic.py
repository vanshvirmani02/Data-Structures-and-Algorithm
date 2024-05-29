n=6 
m=3

arr=[0, 1 ,0 ,0 ,1 ,1]

count = m
max_length=0
for i in range(n):
    if arr[i]==1:
        count+=1
    else:
        max_length=max(max_length,count)
max_length=max(max_length,count)
print(max_length)