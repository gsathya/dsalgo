lists = [[1, 2, 3], [2, 5], [1, 5, 5], [1, 3, 9, 10]]

def find_min_list(lists):
    # lists is empty
    if len(lists) == 0:
        return

    min = len(lists[0])

    # O(n*m) running time
    for l in lists[1:]:
        if min > len(l):
            min = len(l)

    return min

def find_min_list2(lists):
    i = 0
    n = len(lists)

    try:
        while True:
            for x in range(n):
                _ = lists[x][i]
            i += 1
    except IndexError:
        return i

print find_min_list(lists)
print find_min_list2(lists)
