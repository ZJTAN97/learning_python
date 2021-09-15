def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first+last) // 2 # round down to nearest whole number

        if list[midpoint] == target: # constant time operations
            return midpoint
        elif list[midpoint] <= target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list.")


numbers = [x for x in range(11)]
result = binary_search(numbers, 10)

verify(result)