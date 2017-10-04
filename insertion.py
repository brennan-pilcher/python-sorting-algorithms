# Insertion Sort

def insertion_sort ( values ):
    """Insertion sort implementation. Worst case performance of O(n^2)."""
    sorted = values

    index = 1
    while (index < len(sorted)):
        head = index
        while (head > 0 and sorted[head-1] > sorted[head]):
            tmp = sorted[head-1]
            sorted[head-1] = sorted[head]
            sorted[head] = tmp
            head-=1
        index+=1

    return sorted
