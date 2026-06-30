from typing import List

class Solution:
    def insertionSort(self, arr: List[int], n: int) -> List[int]:
        n = len(arr)
        for i in range (1,n):
            key = arr[i]
            j = i-1
            while (j>0 or j==0) and (arr[j]>key):
                arr[j+1] = arr[j]
                j = j-1 # j-=1 can also be used
            arr[j+1] = key # i will automatically shift by 1 and become the new key 
        return arr