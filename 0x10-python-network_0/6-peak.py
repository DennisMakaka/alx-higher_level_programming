#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers efficiently. """

def find_peak(list_of_integers):
    """
    Finds the peak element in a list of integers.

    Args:
        list_of_integers (list): A list of integers to find the peak of.

    Returns: 
        int or None: The peak element of the list, or None if the list is empty
    """
    # Get the size of the list
    size = len(list_of_integers)
    # Initialize variables for mid element and index
    mid_e = size
    mid = size // 2

    # Check if list is empty 
    if size == 0:
        return None

    # Binary search for peak element
    while True:
        mid_e = mid_e // 2
        # Check if mid element is smaller than the next element
        if (mid < size - 1 and 
                list_of_integers[mid] < list_of_integers[mid + 1]):
            # Move mid towards right
            if mid_e // 2 == 0:
                mid_e = 2
            mid = mid + mid_e // 2
        # Check if mid element is smaller than the previous element
        elif mid_e > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            # Move mid towards left
            if mid_e // 2 == 0:
                mid_e = 2
            mid = mid - mid_e // 2
        else:
            return list_of_integers[mid] # Returns peak element
