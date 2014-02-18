def sort(arr):
    if arr == []:
        return []
    
    pivot = arr[0]
    lesser = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]

    return sort(lesser) + [pivot] + sort(greater)

arr = [i for i in reversed(range(10))]
print sort(arr)
