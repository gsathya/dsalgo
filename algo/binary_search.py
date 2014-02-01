def binary_search(arr, item):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = start+(end-start)/2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            start = mid+1
        else:
            end = mid-1

    return False

def begining_search(arr, item):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = start+(end-start)/2
        if arr[mid] >= item:
            end = mid-1
        else:
            start = mid+1

    return start

def end_search(arr, item):
    start = 0
    end = len(arr)

    while start <= end:
        mid = start+(end-start)/2
        if arr[mid] <= item:
            start = mid+1
        else:
            end = mid-1

    return end
