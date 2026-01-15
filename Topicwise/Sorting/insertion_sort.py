def insertion_sort(arr):
    """
    Sorts the given array using the Insertion Sort algorithm.

    Insertion sort is a simple sorting algorithm that builds the final sorted array
    one item at a time. It is much less efficient on large lists than more advanced
    algorithms such as quicksort, heapsort, or merge sort.

    Time Complexity: O(n^2) in worst and average case, O(n) in best case
    Space Complexity: O(1)

    Args:
        arr (list): The list of elements to be sorted (in-place)

    Returns:
        list: The sorted list
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
if __name__ == "__main__":
    # Test cases
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [1, 2, 3, 4, 5],  # Already sorted
        [5, 4, 3, 2, 1],  # Reverse sorted
        [],  # Empty array
        [42]  # Single element
    ]

    for arr in test_arrays:
        original = arr.copy()
        sorted_arr = insertion_sort(arr)
        print(f"Original: {original} -> Sorted: {sorted_arr}")
