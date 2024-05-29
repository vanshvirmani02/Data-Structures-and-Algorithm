#Brute ForCe
'''a = [1,2,2,3,3,3,4,4,5,5 ]
temp=[]

for i in a:
    if i not in temp:
        temp.append(i)
a[:]=temp
print(a)
'''
# Optimal for LEETcode

arr=[0,0,0,1,1,2,2,3,3,4]

n=len(arr)
count=1
i=0
j=i+1
if n==1:
    print(arr)
while j<n:
    if arr[i]==arr[j]:
        j+=1
    else:
        i+=1
        arr[i],arr[j]=arr[j],arr[i]
        j+=1
        count+=1
print(count)
