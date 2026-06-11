#counting the number of individual ints in a given int 

num = 5873
count = 0 #initalization 
while num > 0:
    count = count + 1 #for actual counting 
    num = num//10 #floor divison for num traversal 
    
print(count)