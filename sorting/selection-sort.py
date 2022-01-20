'''
Merge sort
Time complexity: worst case - O(n^2)
Not an in-place sorting algo
pseudocode
selectionsort(n):
    for i <--- 0 to length(n)-2
        minvalindex = i
        for j in i+1 to length(n):
            if n[j] < n[minvalindex]
                minvalindex <--- j
        temp <--- n[i]
        n[i] <--- n[minvalindex]
        n[minvalindex] <--- temp
        
'''

def selection_sort(n):
    for i in range(len(n)-1):
        minval = i
        for j in range(i+1,len(n)):
            if n[j] < n[minval]:
                minval = j
        temp = n[i]
        n[i] = n[minval]
        n[minval] = temp
    return n

print(selection_sort([6,9,4,0,3,1,9,6,99,7]))