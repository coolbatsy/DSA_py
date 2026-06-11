n = [1,2,2,2,4,5,6,7,8,9,10,10,1,5,3]
m =[23,34,5,67,67,89,56,90,84,56,4,5]

hash_arr = [0]*11
for i in n:
    hash_arr[i]+=1

for i in m:
    if i<1 or i>10:
        print(0)

    else:
        print(hash_arr[i])
        