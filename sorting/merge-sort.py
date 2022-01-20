'''
Merge sort
Time complexity: worst case - O(nlogn), beast case-linearithmic
Space complexity: O(n)
Space complexity: if extra arrays are not cleared: O(nlogn), if extra arrays are cleared: O(n)

'''
def merge(L,R,n):
    nL = len(L)
    nR = len(R)
    i = j = k = 0
    while  i < nL and j < nR:
        if L[i] < R[j]:
            n[k] = L[i]
            i += 1
        else:
            n[k] = R[j]
            j += 1
        k += 1
    while i < nL:
        n[k] = L[i]
        i += 1
        k += 1
    while  j < nR:
        n[k] = R[j]
        j += 1
        k += 1

def merge_sort(n):
    arrsize = len(n)
    if arrsize < 2:
        return n
    midpoint = len(n)//2
    left = n[:midpoint]
    right = n[midpoint:len(n)]
    for i in range(midpoint):
        left[i] = n[i]
    for i in range(midpoint,len(n)):
        right[i-midpoint] = n[i]
    merge_sort(left)
    merge_sort(right)
    merge(left,right,n)
    return n

n = [9,8,60,6,3,1,5,7]
print(merge_sort(n))

