# Merge Sort

def merge_sort( values ):
    """Merge sort implementation. O(n log n) worst case performance, but requies up to O(n) additional storage space while sorting."""
    #print ("Splitting: ", values)
    if len(values) > 1:
        middle = len(values) // 2 # integer division
        left = values[:middle] # slicing the array in halves
        right = values[middle:]

        merge_sort(left)
        merge_sort(right)

        left_head = 0
        right_head = 0
        index = 0

        while left_head < len(left) and right_head < len(right): # loop through both halves, comparing values and adding the smallest at position index
            if left[left_head] < right[right_head]:
                values[index] = left[left_head]
                left_head+=1
            else:
                values[index] = right[right_head]
                right_head+=1
            index+=1

        while left_head < len(left):
            values[index] = left[left_head]
            left_head+=1
            index+=1

        while right_head < len(right):
            values[index] = right[right_head]
            right_head+=1
            index+=1

    #print("Merging: ", values)
