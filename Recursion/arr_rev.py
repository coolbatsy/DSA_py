
    
def main(array, left, right):
    if left > right or left == right: # base condition
        return
    array[left], array[right] = array[right], array[left] # swap logic 
    main(array, left+1, right-1) # flow logic 

array = [23,45,67,98,44]
main(array, 0, len(array)-1) # actual reverse perform
print(array)


