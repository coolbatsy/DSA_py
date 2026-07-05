class Solution:

    def quickSort(self, arr, low, high):        
        if low < high: 
            partition_index = self.partition(arr, low, high)
            self.quickSort(arr, low, partition_index-1)
            self.quickSort(arr, partition_index+1, high)
            
    def partition(self, arr, low, high):        
        pivot = arr[low]
        i = low 
        j = high

        while i<j: #by array index 

            while arr[i] <= pivot and i <= high-1:
                i+=1
                
            while arr[j] >= pivot and j >= low+1:
                j-=1
            
            if i<j:
                arr[i], arr[j] = arr[j], arr[i] #swap logic for i and j 
                
        arr[low], arr[j] = arr[j], arr[low]
        return j
                
# Complexities: TC: Best n Avg: O(nlogn), worst: O(n^2), SC: O(1)


        