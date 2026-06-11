#extracting individual ints using loops 
num = 5873
while num > 0:
    last_dig = num%10 #remainder
    print(last_dig)
    num = num//10 #floor division to eleminate float

    
