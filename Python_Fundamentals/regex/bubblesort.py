def selection_sort(arr):
    for i in range(len(arr)):
        larger = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[larger]:
                larger = j
        swap(arr, larger, i)
    return arr 

def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

a = [5,2,3,7,7,9,12,14,2]

selection_sort(a)
print a
