def sequential_max(arr):
    if not arr:
        raise ValueError("Array is empty")
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value