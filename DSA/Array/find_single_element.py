#Brute Force
arr= [1, 1, 2, 3, 3, 4, 4]
my_dict=dict()

for i in arr:
    if i not in my_dict:
        my_dict[i]=1
    else:
        my_dict[i]+=1

for key,value in my_dict.items():
    if value==1:
        print(key)


#Optimal -> To be Told

# my code

'''freq=1

while i<n:
    if arr[i+1]==num:
        freq += 1 
    else:
        min_freq=min(min_freq,freq)
        min_value = _________ 
        num=arr[i+1]
        freq=1
    i+=1'''