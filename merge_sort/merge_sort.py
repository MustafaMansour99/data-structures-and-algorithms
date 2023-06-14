
"""
in this lab used two functions first one to slice the list for left and right the first section take the array from first to the mid and the second from mid to the end of array, and the second function to compare with the left and right value
"""
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(left, right, arr)
    return arr

def merge(left, right, arr):
    i = 0
    j =0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    # if i ==len(left):
    #     arr[k:]=right[j:]
    # else:
    #     arr[k:]=left[i:]

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
arr = [5, 1, 9, 3, 7, 2, 8, 4]
merge_sort(arr)
print(arr)