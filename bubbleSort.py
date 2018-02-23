def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
         for j in range(n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr 

# tests

arr1 = [100, 34, 25, 12, 22, 11, 90] 
print(bubbleSort(arr1))
arr2 = [0,1,0,1,0]
print(bubbleSort(arr2))