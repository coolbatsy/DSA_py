# sum of n natural numbers: 
n = 56
def func(n):
    if n == 1:
        return 1
    return n + func(n-1)

x = func(n)      # ← Store result OUTSIDE the function
print(x)
