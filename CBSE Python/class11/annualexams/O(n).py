#This is the Project comparing both bubble sort and merge sort
#This is Bubble Sort.Bubble sort
import time
arr=[1,2,7,3,6,5,6,7,9,9,3,4234,234234,24,2,34,234,34,24,24,4,5,6,7,8,98,9,90,12,89,89,76,54,78,76,2525,28282,282828,292929,34,67,891,2,7,3,6,5,6,7,9,9,3,4234,234234,24,2,34,234,34]
#This is given by me and user input can be given
n = len(arr)#This is the length of arr
tstart = time.time()
for i in range(n): 
    for j in range(0, n-i-1): 
        if arr[j] > arr[j+1] : 
            arr[j], arr[j+1] = arr[j+1], arr[j] 
tend = time.time()
print(tstart)#This is to check start time 
print(tend)#This to check the end time of the program
print('Total time to execute:\t', tend - tstart)#This is the time period of the list 
print("Bubble sort",arr)
#This is insertion sort using an array of insertion sort 
def insertion_sort(arr):
    for i in range(1, len(arr)):#Looping the element for arrr
        # This is the element we want to position in its correct place
        a = arr[i]
        j=i-1
        # Create a variable that will be used to find the correct position of i and it will be used with respect to a 
        while j >= 0 and arr[j] > a:
            # Shift the value one position to the left and reposition j to point to the next element from the right to the left
            arr[j + 1] = arr[j]
            j-=1

        # When you finish shifting the elements, you can position
        # `a` in its correct location
        arr[j + 1] = a
tend = time.time()
print(tstart)#This 
print(tend)#This to check the end time of the program
print('Total time to execute:\t', tend - tstart)#This is the time period of the list 
print("Insertion Sort",arr)
#From the output its clear that insertion sort is a efficent algorithm the time 


