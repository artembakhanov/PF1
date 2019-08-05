def naive_reverse(a):
    """Naive reverse (not in place)"""
    new = [] # create an empty list
    n = len(a)
    for i in range(n - 1, -1, -1): # iterate from n-1 to 0 (from the end to the start)
        new.append(a[i]) # add to the new list
    return new


def nice_reverse(a):
    """Reverse in place"""
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i] # really nice way to swap values!
    return a # you do not need to return anything cause list is passed by reference


test = input().split()
print(*naive_reverse(test))
print(*nice_reverse(test))

# you can also use reversed() and solve this task is one line
print(*reversed(input().split()))
