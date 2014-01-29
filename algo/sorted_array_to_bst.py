from lib import bst

def convert(arr, start, end, bst):
    if start > end:
        return

    mid = start+(end-start)/2

    bst.add(arr[mid])
    convert(arr, start, mid-1, bst)
    convert(arr, mid+1, end, bst)
