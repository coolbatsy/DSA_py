n = [12,13,14,9,9087,45,56,3,45,67,4]
m = [3,45,67,0,45,678,90,23,1,56,14,9]

hash_map = {}

# we have to check how many elements of m are in n and their frequency 
for i in n:
    if(i in hash_map):
        hash_map[i]+=1
    else:
        hash_map[i]=1

for i in m:

    if i in hash_map:
        print(hash_map[i])
    else:
        print(0)

    
