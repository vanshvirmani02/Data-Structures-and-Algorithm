# LIFO - Last in First Out
# Print N times in recursion 
# TC=O(N+1) ~ O(N)
# SC=O(N+1) ~ O(N)

#print 1 to N (without backtracking)
def printn(i,n):
    if i>n:
        return 
    print(i)
    printn(i+1,n)



#print N to 1 (without backtracking)
def func(n):
    if n==0:
        return
    print(n)
    func(n-1)

func(5)


# Homeword N--> 1 
# with i+1