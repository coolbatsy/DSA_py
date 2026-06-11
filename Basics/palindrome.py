n = 1234
num = n #storing n in num 
result = 0 #initialization

while num > 0: 
    last_dig = num % 10
    result = (result*10)+last_dig
    num = num//10

if(n==result):
    print(True)

else:
    print(False)
