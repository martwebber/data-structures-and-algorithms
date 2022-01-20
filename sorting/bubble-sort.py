'''
Bubble sort
Time complexity: best case - O(n), average case - O(n^2) worst case - O(n^2)
pseudocode
bubblesort(n):
    for i <--- 1 to length(n)-1
        for j <--- 0 to length(n)-2
            if n[i] > n[i+1]
                swap(n[i],n[i+1])
'''
def bubble_sort(n):
    swap_rounds = 0
    for j in range(1,len(n)):
        for i in range(len(n)-j):
            if n[i] > n[i+1]:
                n[i], n[i+1] = n[i+1],n[i]
                swap_rounds +=1
    return (n,swap_rounds)

n = [266,9,8,60,6,2,1,7]
print(bubble_sort(n))
