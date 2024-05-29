def armstrong(n):
    lamba=len(str(n))
    total = 0
    temp_num=n
    while n>0:
        ld = n%10
        total += ld ** lamba
        n=n//10
    
    if total==temp_num:
        return True
    else:
        return False
print(armstrong(371))
print(armstrong(371))