# Selection Sort

def selection_sort( values ):
    sorted = values

    for index in range(0, len(sorted)-1):
        """Selection sort implementation. N swaps with worst case performance of O(n^2)."""
        min = index
        for subindex in range(index+1, len(sorted)):
            if sorted[subindex] < sorted[index] :
                min = subindex
        if min != index:
            tmp = sorted[index]
            sorted[index] = sorted[min]
            sorted[min] = tmp
    return sorted
