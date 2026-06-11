n = "wufuegdguednuyusdfqbjebjk"
m = ["d","y","j","w","t","z"]

hash_arr = [0]*27

# only lower case alpahbets allowed 

for i in n: 
    ascii_val = ord(i)
    index = ascii_val-97 # as a is at 97 in ASCII
    hash_arr[index]+=1

for i in m:
    ascii_val = ord(i)
    index = ascii_val-97
    print(hash_arr[index])

