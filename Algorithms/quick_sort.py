def quick_sort(lst):
    if len(lst) < 2:
        return lst
    
    else:
        pivot = lst[0]
        lesser = [item for item in lst[1:] if item <= pivot]
        greater = [item for item in lst[1:] if item > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


print(quick_sort([10, 5, 3, 2]))