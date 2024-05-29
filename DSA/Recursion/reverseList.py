   
def reverse_list(lst, start, end):
    if start > end:
        return 
    lst[start], lst[end] = lst[end], lst[start]
    reverse_list(lst, start + 1, end - 1)    
    return lst

lst=[1,2,3,4,5]
n=len(lst)
print(reverse_list(lst,0,n-1))