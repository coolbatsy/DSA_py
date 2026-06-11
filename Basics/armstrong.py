n = 153
num = n 
total = 0
nofd = len(str(n)) #typecasted n in string for using str len func

while num > 0:
    last_dig = num%10
    total = total + (last_dig**nofd)
    num = num//10

if(n==total):
    print(True)

else:
    print(False)
