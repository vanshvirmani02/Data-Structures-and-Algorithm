#Optimal Solution
'''
Time complexity : O(Log10 N)
Space complexity: O(1)
'''


def palindrome(x):
    if x<0:
        return False 
    num = x
    reverse_num = 0
    while num > 0:
        last_digit = num % 10 
        reverse_num = reverse_num * 10 + last_digit
        num = num // 10
    return reverse_num == x

print(palindrome(121))
print(palindrome(-121))
print(palindrome(10))