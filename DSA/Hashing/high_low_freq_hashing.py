arr=[1,2,3,1,1,4]
my_dict=dict()
for i in arr:
    if i not in my_dict:
        my_dict[i]=1
    else:
        my_dict[i]+= 1 
print(my_dict)


max_freq=float('-inf')
max_key= float('inf')
min_freq=float('inf')
min_key=float('inf')

for key,freq in my_dict.items():
    if freq>max_freq or freq==max_freq and key<max_key:
        max_freq=freq
        max_key = key
    if freq<min_freq or freq==min_freq and key<min_key:
        min_freq=freq
        min_key = key
print(max_key,min_key)
