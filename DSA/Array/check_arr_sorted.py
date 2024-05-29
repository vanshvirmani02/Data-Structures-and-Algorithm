#Solution of Coding Ninjas
'''def issorted(a,n):
    flag=1

    for i in range(n-1):
        if a[i]>a[i+1]:
            flag= 0

    return flag

a=[1, 2,  4,3, 5]
n=len(a)
print(issorted(a,n))
'''

#Solution for Leetcode 
#Q-Find the array is sroted or not even if it is rotated

'''def issorted(numbs):
    n=len(numbs)
    rotation = 0
    for i in range(0,n):
        if numbs[i]>numbs[(i+1)%n]:
            rotation += 1 
            if rotation>1:
                return False
    return True

# numbs=[5,6,1,2,3,4] --> True
# numbs=[6,8,9,4,5,7]  --> False

print(issorted(numbs))'''