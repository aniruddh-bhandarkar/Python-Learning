import time
arr=[1,2,7,3,6,5,6,7,9,9,3,4234,234234,24,2,34,234,34,24,24,4,5,6,7,8,98,9]
n = len(arr)
tstart = time.time()
for i in range(n-1):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            '''temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp'''
tend = time.time()
print(tstart)
print(tend)
print('Total time to execute', tend - tstart)
print(arr)

