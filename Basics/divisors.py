# writing all the divisors of a given num in an array/list

#optimal solution 

from math import sqrt

n = 55
num = n
divisors = []

for i in range(1,int(sqrt(num))+1):

    if (num%i) == 0:
        divisors.append(i)
    
        if (num//i) != i:
            divisors.append(num//i)
    
divisors.sort()
print(divisors)

#Brute Force: Traverse all 
#Better: Traverse half + append the num itself 
