arr=[1,3,1,2,7,9]
hash_list=[0]*6

for i in range(len(arr)):
    if arr[i]<6:
        hash_list[arr[i]-1] += 1 
print(hash_list)











































































'''# n=number of elements
# # m= till m tk  
# arr = [1, 3, 1, 9, 2, 7] 

# my_dict=dict()

# for i in arr:
#     if i not in my_dict:
#         my_dict[i] = 1
#     else:
#         my_dict[i] += 1  

# for key,value in my_dict.items():
#     print(value,end=" ")


def countFrequency(n: int, m: int, arr):
    my_dict=dict()

    for i in arr:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1  

    for key,value in my_dict.items():
        print(value, end=" ") 

countFrequency(6,9,arr=[1,3,1,9,2,7])'''