num = 5
def fact(num):
    if num == 0 or num == 1: #base case
        return 1
    return num*fact(num-1) #flow

factorial = fact(num)
print("factorial: ", factorial)
