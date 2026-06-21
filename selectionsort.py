
# sorting in descending order 
arr = [34,56,8,12,90,45]

n = len(arr) # for easy traversal 

for i in range(0,n):
    min_ind = i
    for j in range(i+1,n):
        if arr[j] > arr[min_ind]:
            min_ind = j
        
    arr[i],arr[min_ind]=arr[min_ind],arr[i] #swap logic 
print(arr)



