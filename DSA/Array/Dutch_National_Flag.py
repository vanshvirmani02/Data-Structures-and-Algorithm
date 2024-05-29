# Brute Force

# arr=[2, 2, 2, 2, 0, 0, 1, 0]

'''arr.sort()
print(arr)

'''
##########################################################################################

#Better Solution 

#Approach 1

'''count_0=0
count_1=0
count_2=0
n=len(arr)
temp=[]
for i in range(n):
    if arr[i]==0:
        count_0+=1
    elif arr[i]==1:
        count_1+=1
    elif arr[i]==2:
        count_2+=1

for i in range(0,count_0+1):
    temp.append(0)
for i in range(count_0,count_0+count_1):
    temp.append(1)
for i in range(count_1+count_0,n):
    temp.append(2)
print(temp)'''

#Aproach 2 


'''count_0=0
count_1=0
count_2=0
n=len(arr)
temp=[]
for i in range(n):
    if arr[i]==0:
        count_0+=1
    elif arr[i]==1:
        count_1+=1
    elif arr[i]==2:
        count_2+=1

temp=[0]*count_0+[1]*count_1+[2]*count_2
print(temp)'''

######################################################################################################

#Optimal Solution

arr=[2, 2, 2, 2, 0, 0, 1, 0]
n=len(arr)
mid,low=0,0
high=n-1

while mid<=high:
    if arr[mid]==0:
        arr[low],arr[mid]=arr[mid],arr[low]
        mid+=1
        low+=1
    elif arr[mid]==1:
        mid+=1
    elif arr[mid]==2:
        arr[high],arr[mid]=arr[mid],arr[high]
        high-=1
    
print(arr)
