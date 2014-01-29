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

def beg_search(arr, item):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = start+(end-start)/2
        if arr[mid] <= item:
            start = mid+1
        else:
            end = mid-1

    return start

def end_search(arr, item):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = start+(end-start)/2
        if arr[mid] >= item:
            end = mid-1
        else:
            start = mid+1

    return start, end

arr = [0, 1, 2, 3, 4, 4, 4, 10]
print arr
print end_search(arr, 4)
            
    
