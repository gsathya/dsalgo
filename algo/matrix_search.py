
def find_row(rows, item):
    start = 0
    end = len(rows)-1
    
    while start < end:
        mid = start+end/2
        if rows[mid] >= item:
            end = mid-1
        else:
            start = mid+1
    return start

def find(rows, item):
    start = 0
    end = len(rows)-1
    
    while start <= end:
        mid = start+end/2
        if rows[mid] == item:
            return mid
        elif rows[mid] > item:
            end = mid-1
        else:
            start = mid+1
    
    return -1

def find(matrix, item):
    rows = []

    for i in range(len(matrix[0])):
        rows.append(matrix[0][i])
        
    row = find_row(rows, item)
    col1 = find(matrix[row], item)
    col2 = find(matrix[row+1], item)
    
    return matrix[row][col1] if col2==-1 else matrix[row+1][col2]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print find(matrix, 3)
