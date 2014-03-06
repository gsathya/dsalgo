def comb(arr, r):
    data = [0]*(r)
    
    combUtil(arr, data, 0, 0, r)
    
def combUtil(arr, data, index, i, r):
    if index == r:
        print data
        return
        
    if i == len(arr):
        return
        
    data[index] = arr[i]
    
    combUtil(arr, data, index+1, i+1, r)
    
    combUtil(arr, data, index, i+1, r)
    
comb([1, 2, 3, 4, 5], 3)
