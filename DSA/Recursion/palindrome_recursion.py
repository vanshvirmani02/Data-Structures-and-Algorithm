def ispallindrome(word,i):
    if i >= len(word)//2:
        return True
    if word[i]!= word[len(word)-i-1]:
        return False
    ispallindrome(word,i+1)
    return True

# print(ispallindrome("vansh",0))
word = "malayalam"
print(ispallindrome(word,0))