def is_palindrome(str):
    """Checks whether the given string is a palindrome"""
    n = len(str)
    for i in range(n // 2):
        if str[i] != str[n - i - 1]:
            return False
    return True


print(is_palindrome("Hello world"))
print(is_palindrome("madam"))
print(is_palindrome("racecar"))
print(is_palindrome("ABBA"))
