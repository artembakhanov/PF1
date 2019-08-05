n = int(input("Enter a number >> "))
sum = 0 # variable that stores sum from 1 to n
for i in range (1, n + 1): # iterate from 1 to n (included)
    sum += i # add i to the sum

# this is an example of formatting output in Python
print("Sum of the numbers from 1 to %d is %d" % (n, sum))

# this problem can be solved without any loops
# just use math:)
print("Sum of the numbers from 1 to %d is %d (without loops)" % (n, n * (n + 1) // 2))