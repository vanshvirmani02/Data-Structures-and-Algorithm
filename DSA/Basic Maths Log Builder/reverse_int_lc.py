# Brute Force
# and Optimal
"""
Time Complexity = O(log10 n), n is the number
Space Complexity = O(1)
"""


def reverse( x: int) -> int:
    num = abs(x) 
    reverse_num = 0
    while num >0:
        last_digit = num % 10 
        reverse_num = reverse_num * 10 + last_digit
        num = num // 10
    if  x < 0:
        reverse_num = reverse_num * -1
    if reverse_num< (-(2**31)) or reverse_num > (2**31 - 1):
        return 0 
    return reverse_num


print(reverse(-123))