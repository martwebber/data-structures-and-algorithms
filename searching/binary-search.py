"""
Time complexity: best case - O(1) , worst case - O(logn)
pseudocode
binarysearch(n,val)
    start <--- 0
    end <--- length(n)-1
    while start <= end:
        mid <--- (start + end)/2
            if n[mid]  == val:
                return mid
            elif val < n[mid]:
                end <--- mid-1
            else:
                start <--- mid+1
    return -1

"""

def binary_search(n,val):
    start = 0
    end = len(n)-1
    while start <= end:
        midpoint = (start+end)//2
        if n[midpoint] == val:
            return midpoint
        elif val < n[midpoint]:
            end = midpoint - 1
        else:
            start = midpoint + 1
    return 'element not found'

print(binary_search([i for i in range(11)],5))
print(binary_search([i for i in range(11)],12))