def insertion_sort(arr):
    """
    Sorts an input list in ascending order using the Insertion Sort algorithm.

    Args:
        input (list): The input list to be sorted.

    Returns:
        list: The sorted list in ascending order.

    Examples:
        >>> arr = [20, 18, 12, 8, 5, -2]
        >>> sorted_arr = insertion_sort(arr)
        >>> print(sorted_arr)
        [-2, 5, 8, 12, 18, 20]
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
def insert(sorted, value):
    """
    Inserts a value into the sorted list at the appropriate position.

     Args:
        sorted (list): The sorted list to insert the value into.
        value (int): The value to be inserted.
    """

    i = 0

    while i < len(sorted) and value > sorted[i]:
        i += 1

    sorted.append(None)
    j = len(sorted) - 1

    while j > i:
        sorted[j] = sorted[j - 1]
        j -= 1

    sorted[i] = value

# Example
arr = [20,18,12,8,5,-2]
sorted_arr = insertion_sort(arr)
print(sorted_arr)
#output [-2, 5, 8, 12, 18, 20]