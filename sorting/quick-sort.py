'''
Quick sort 
Time complexity: Best case-O(nlogn),Average case-O,worst case-O(n^2)

Pseudocode
Quicksort(arr,start,end)
    if start < end
        partitionIndex <--- partition(arr,start,end)
        Quicksort(arr,start,partitionIndex - 1)
        Quicksort(arr,start,partitionIndex + 1, end)
Partition(arr,start,end)
    pivot <-- A[end]
    partitionIndex <-- start
    for i <-- start to end - 1
        if arr[i] <= pivot
            swap(arr[i],arr[partitionIndex])
            PartitionIndex <-- PartitionIndex + 1
    swap(arr[PartitionIndex],arr[end])
    return PartitionIndex                                                                                    
'''

def quickSort(arr,start,end):
    if start < end:
        partitionIndex = partition(arr,start,end)
        quickSort(arr,start, partitionIndex-1)
        quickSort(arr,partitionIndex+1,end)

def partition(arr,start,end):
    pivot = arr[end]
    partitionIndex = start-1
    for i in range(start,end):
        if arr[i] < pivot:
            partitionIndex += 1  
            arr[i],arr[partitionIndex] = arr[partitionIndex],arr[i]
    arr[end],arr[partitionIndex+1] = arr[partitionIndex+1],arr[end]
    return partitionIndex+1

arr = [2,0,5,3,8,1,9,6]
start = 0
end = len(arr)-1
quickSort(arr,start,end)
print(arr)