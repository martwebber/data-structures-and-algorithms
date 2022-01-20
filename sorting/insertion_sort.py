'''
Insertion sort - it is an in-place sorting algorithm
Time complexity: best case - O(n),average case- O(n^2) worst case - O(n^2)
Better time complexity than bubble and selection sort
pseudocode
insertionsort(n)

'''

def insertion_sort(n):
    for i in range(1,len(n)):
        value = n[i]
        hole = i
        while hole > 0 and n[hole-1] > value:
            n[hole] = n[hole-1]
            hole = hole-1
        n[hole] = value
    return n
print(insertion_sort([6,4,0,3,5,9,8]))