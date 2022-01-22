# Reverse Array In-place
# solution 1
import  array as arr
def reverseArray(A):
    for val in A[::-1]:
        print(val)

myarr = arr.array('i',[1,2,3,4,5])
reverseArray(myarr)

# solution 2

def reverseArray2(A):
    print(reverse(A))

myarr2 = arr.array('i',[1,2,3,4,5])
reverseArray(myarr2)

# Solution 3 
def reverseArray3(A):
    start = 0
    
    stop = len(A)-1
    while start < stop:
        A[start], A[stop] = A[stop], A[start]
        start += 1
        stop -= 1
    print(A)

myarr3 = arr.array('i',[1,2,3,4,5])
reverseArray3(myarr3)