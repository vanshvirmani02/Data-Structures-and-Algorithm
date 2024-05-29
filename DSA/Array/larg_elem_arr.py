arr = [1, 2, 3, 4, 5]
n=len(arr)
max_element=arr[0]
for i in range(n):
    if arr[i]>max_element:
        max_element=arr[i]
print(max_element)
