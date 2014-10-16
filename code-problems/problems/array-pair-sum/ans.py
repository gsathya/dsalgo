def find_pair(sum, array):
    seen = {}
    pairs = []

    for num in array:
        diff = sum - num

        if diff in seen:
            for i in range(seen[diff]):
                pairs.append((num, diff))

        seen[num] = seen.get(num, 0) + 1

    return pairs

print find_pair(10, [3, 4, 5, 6, 7])
print find_pair(8, [3, 4, 5, 4, 4])
