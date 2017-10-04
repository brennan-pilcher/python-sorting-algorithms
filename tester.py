# Sort Tester
#
# Used to feed data into the various sorting algorithms.

# Imports
from insertion import insertion_sort

short_list = [5, 1, 3, 2, 4, 7, 6, 8, 9, 0]

print( *insertion_sort(short_list) )
